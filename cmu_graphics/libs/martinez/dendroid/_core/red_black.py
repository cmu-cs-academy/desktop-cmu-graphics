from __future__ import annotations

import copy
import weakref
from collections.abc import Iterable
from reprlib import recursive_repr
from typing import Any, Generic, Self, cast, overload

from cmu_graphics.libs.martinez.reprit.base import generate_repr

from . import abcs
from .hints import Item, KeyT, ValueT
from .nil import NIL, Nil
from .utils import (
    dereference_maybe,
    maybe_weakref,
    to_balanced_tree_height,
    to_unique_sorted_items,
    to_unique_sorted_values,
)


class Node(abcs.HasCustomRepr, Generic[KeyT, ValueT]):
    @property
    def item(self, /) -> Item[KeyT, ValueT]:
        return self.key, self.value

    @property
    def key(self, /) -> KeyT:
        return self._key

    @property
    def left(self, /) -> Self | Nil:
        return self._left

    @left.setter
    def left(self, value: Self | Nil, /) -> None:
        self._left = value
        _set_parent(value, self)

    @property
    def parent(self, /) -> Self | Nil:
        return dereference_maybe(self._parent)

    @parent.setter
    def parent(self, value: Self | Nil, /) -> None:
        self._parent = maybe_weakref(value)

    @property
    def right(self, /) -> Self | Nil:
        return self._right

    @right.setter
    def right(self, value: Self | Nil, /) -> None:
        self._right = value
        _set_parent(value, self)

    @property
    def value(self, /) -> ValueT:
        return self._value

    @value.setter
    def value(self, value: ValueT) -> None:
        self._value = value

    _left: Self | Nil
    _right: Self | Nil
    _parent: weakref.ref[Self] | Nil

    __slots__ = (
        '__weakref__',
        '_key',
        '_left',
        '_parent',
        '_right',
        '_value',
        'is_black',
    )

    def __init__(
        self,
        key: KeyT,
        value: ValueT,
        /,
        *,
        is_black: bool,
        left: Self | Nil = NIL,
        right: Self | Nil = NIL,
        parent: Self | Nil = NIL,
    ) -> None:
        self._key, self._value, self.is_black = key, value, is_black
        self.left, self.right, self.parent = left, right, parent

    __repr__ = recursive_repr()(generate_repr(__init__))

    def __getstate__(self, /) -> tuple[Any, ...]:
        return (
            self._key,
            self.value,
            self.is_black,
            self.parent,
            self.left,
            self.right,
        )

    def __setstate__(self, state: tuple[Any, ...]) -> None:
        (
            self._key,
            self._value,
            self.is_black,
            self.parent,
            self._left,
            self._right,
        ) = state


def _set_parent(
    node: Node[KeyT, ValueT] | Nil, parent: Node[KeyT, ValueT] | Nil
) -> None:
    if node is not NIL:
        node.parent = parent


def _set_black(node: Node[KeyT, ValueT] | Nil, /) -> None:
    if node is not NIL:
        node.is_black = True


def _is_left_child(node: Node[KeyT, ValueT], /) -> bool:
    parent = node.parent
    return parent is not NIL and parent.left is node


def _is_node_black(node: Node[KeyT, ValueT] | Nil, /) -> bool:
    return node is NIL or node.is_black


class Tree(abcs.Tree[KeyT, ValueT]):
    @overload
    @classmethod
    def from_components(
        cls, keys: Iterable[KeyT], values: None = ..., /
    ) -> Tree[KeyT, KeyT]: ...

    @overload
    @classmethod
    def from_components(
        cls, keys: Iterable[KeyT], values: Iterable[ValueT], /
    ) -> Self: ...

    @classmethod
    def from_components(
        cls: type[Tree[KeyT, KeyT]] | type[Tree[KeyT, ValueT]],
        _keys: Iterable[KeyT],
        values: Iterable[ValueT] | None = None,
        /,
    ) -> Tree[KeyT, KeyT] | Tree[KeyT, ValueT]:
        keys = list(_keys)
        if not keys:
            return cls(NIL)
        if values is None:
            keys = to_unique_sorted_values(keys)

            def to_simple_node(
                start_index: int,
                end_index: int,
                depth: int,
                height: int = to_balanced_tree_height(len(keys)),
                /,
            ) -> Node[KeyT, KeyT]:
                middle_index = (start_index + end_index) // 2
                key = keys[middle_index]
                return Node(
                    key,
                    key,
                    is_black=depth != height,
                    left=(
                        to_simple_node(start_index, middle_index, depth + 1)
                        if middle_index > start_index
                        else NIL
                    ),
                    right=(
                        to_simple_node(middle_index + 1, end_index, depth + 1)
                        if middle_index < end_index - 1
                        else NIL
                    ),
                )

            simple_root = to_simple_node(0, len(keys), 0)
            simple_root.is_black = True
            return cast(type[Tree[KeyT, KeyT]], cls)(simple_root)
        items = to_unique_sorted_items(keys, tuple(values))

        def to_complex_node(
            start_index: int,
            end_index: int,
            depth: int,
            height: int = to_balanced_tree_height(len(items)),
            /,
        ) -> Node[KeyT, ValueT]:
            middle_index = (start_index + end_index) // 2
            key, value = items[middle_index]
            return Node(
                key,
                value,
                is_black=depth != height,
                left=(
                    to_complex_node(start_index, middle_index, depth + 1)
                    if middle_index > start_index
                    else NIL
                ),
                right=(
                    to_complex_node(middle_index + 1, end_index, depth + 1)
                    if middle_index < end_index - 1
                    else NIL
                ),
            )

        complex_root = to_complex_node(0, len(items), 0)
        complex_root.is_black = True
        return cast(type[Tree[KeyT, ValueT]], cls)(complex_root)

    @property
    def root(self, /) -> Node[KeyT, ValueT] | Nil:
        return self._root

    def clear(self, /) -> None:
        self._root = NIL

    def predecessor(
        self, node: abcs.Node[KeyT, ValueT], /
    ) -> Node[KeyT, ValueT] | Nil:
        assert isinstance(node, Node)
        if node.left is NIL:
            result = node.parent
            while result is not NIL and node is result.left:
                node, result = result, result.parent
        else:
            result = node.left
            while result.right is not NIL:
                result = result.right
        return result

    def successor(
        self, node: abcs.Node[KeyT, ValueT], /
    ) -> Node[KeyT, ValueT] | Nil:
        assert isinstance(node, Node), node
        if node.right is NIL:
            result = node.parent
            while result is not NIL and node is result.right:
                node, result = result, result.parent
        else:
            result = node.right
            while result.left is not NIL:
                result = result.left
        return result

    def insert(self, key: KeyT, value: ValueT, /) -> Node[KeyT, ValueT]:
        parent = self._root
        if parent is NIL:
            node = self._root = Node(key, value, is_black=True)
            return node
        while True:
            if key < parent.key:
                if parent.left is NIL:
                    node = Node(key, value, is_black=False)
                    parent.left = node
                    break
                parent = parent.left
            elif parent.key < key:
                if parent.right is NIL:
                    node = Node(key, value, is_black=False)
                    parent.right = node
                    break
                parent = parent.right
            else:
                return parent
        self._restore(node)
        return node

    def remove(self, node: abcs.Node[KeyT, ValueT], /) -> None:
        assert isinstance(node, Node), node
        successor, is_node_black = node, node.is_black
        if successor.left is NIL:
            (
                successor_child,
                successor_child_parent,
                is_successor_child_left,
            ) = (successor.right, successor.parent, _is_left_child(successor))
            self._transplant(successor, successor_child)
        elif successor.right is NIL:
            (
                successor_child,
                successor_child_parent,
                is_successor_child_left,
            ) = (successor.left, successor.parent, _is_left_child(successor))
            self._transplant(successor, successor_child)
        else:
            assert node.right is not NIL
            successor = node.right
            while successor.left is not NIL:
                successor = successor.left
            is_node_black = successor.is_black
            successor_child, is_successor_child_left = successor.right, False
            if successor.parent is node:
                successor_child_parent = successor
            else:
                is_successor_child_left = _is_left_child(successor)
                successor_child_parent = successor.parent
                self._transplant(successor, successor.right)
                successor.right = node.right
            self._transplant(node, successor)
            assert node.left is not NIL
            node.left.parent = successor
            successor.left, successor.is_black = node.left, node.is_black
        if is_node_black:
            self._remove_node_fixup(
                successor_child,
                successor_child_parent,
                is_successor_child_left,
            )

    def _restore(self, node: Node[KeyT, ValueT], /) -> None:
        while not _is_node_black(node.parent):
            parent = node.parent
            assert parent is not NIL
            grandparent = parent.parent
            assert grandparent is not NIL
            if parent is grandparent.left:
                uncle = grandparent.right
                if _is_node_black(uncle):
                    if node is parent.right:
                        self._rotate_left(parent)
                        node, parent = parent, node
                    parent.is_black, grandparent.is_black = True, False
                    self._rotate_right(grandparent)
                else:
                    assert uncle is not NIL
                    parent.is_black = uncle.is_black = True
                    grandparent.is_black = False
                    node = grandparent
            else:
                uncle = grandparent.left
                if _is_node_black(uncle):
                    if node is parent.left:
                        self._rotate_right(parent)
                        node, parent = parent, node
                    parent.is_black, grandparent.is_black = True, False
                    self._rotate_left(grandparent)
                else:
                    assert uncle is not NIL
                    parent.is_black = uncle.is_black = True
                    grandparent.is_black = False
                    node = grandparent
        assert self._root is not NIL
        self._root.is_black = True

    def _remove_node_fixup(
        self,
        node: Node[KeyT, ValueT] | Nil,
        parent: Node[KeyT, ValueT] | Nil,
        is_left_child: bool,  # noqa: FBT001
        /,
    ) -> None:
        while node is not self._root and _is_node_black(node):
            assert parent is not NIL
            if is_left_child:
                sibling = parent.right
                assert sibling is not NIL
                if not _is_node_black(sibling):
                    sibling.is_black, parent.is_black = True, False
                    self._rotate_left(parent)
                    sibling = parent.right
                assert sibling is not NIL
                if _is_node_black(sibling.left) and _is_node_black(
                    sibling.right
                ):
                    sibling.is_black = False
                    node, parent = parent, parent.parent
                    is_left_child = _is_left_child(node)
                else:
                    if _is_node_black(sibling.right):
                        assert sibling.left is not NIL
                        sibling.left.is_black, sibling.is_black = True, False
                        self._rotate_right(sibling)
                        sibling = parent.right
                    assert sibling is not NIL
                    sibling.is_black, parent.is_black = parent.is_black, True
                    _set_black(sibling.right)
                    self._rotate_left(parent)
                    node = self._root
            else:
                sibling = parent.left
                if not _is_node_black(sibling):
                    assert sibling is not NIL
                    sibling.is_black, parent.is_black = True, False
                    self._rotate_right(parent)
                    sibling = parent.left
                assert sibling is not NIL
                if _is_node_black(sibling.left) and _is_node_black(
                    sibling.right
                ):
                    sibling.is_black = False
                    node, parent = parent, parent.parent
                    is_left_child = _is_left_child(node)
                else:
                    if _is_node_black(sibling.left):
                        assert sibling.right is not NIL
                        sibling.right.is_black, sibling.is_black = True, False
                        self._rotate_left(sibling)
                        sibling = parent.left
                    assert sibling is not NIL
                    sibling.is_black, parent.is_black = parent.is_black, True
                    _set_black(sibling.left)
                    self._rotate_right(parent)
                    node = self._root
        _set_black(node)

    def _rotate_left(self, node: Node[KeyT, ValueT]) -> None:
        replacement = node.right
        assert replacement is not NIL
        self._transplant(node, replacement)
        node.right, replacement.left = replacement.left, node

    def _rotate_right(self, node: Node[KeyT, ValueT]) -> None:
        replacement = node.left
        assert replacement is not NIL
        self._transplant(node, replacement)
        node.left, replacement.right = replacement.right, node

    def _transplant(
        self,
        origin: Node[KeyT, ValueT],
        replacement: Node[KeyT, ValueT] | Nil,
        /,
    ) -> None:
        parent = origin.parent
        if parent is NIL:
            self._root = replacement
            _set_parent(replacement, NIL)
        elif origin is parent.left:
            parent.left = replacement
        else:
            parent.right = replacement

    _root: Node[KeyT, ValueT] | Nil

    __slots__ = ('_root',)

    def __copy__(self, /) -> Self:
        return type(self)(copy.deepcopy(self._root))

    def __init__(self, root: Node[KeyT, ValueT] | Nil) -> None:
        self._root = root
