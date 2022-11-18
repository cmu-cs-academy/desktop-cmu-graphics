import math
import copy
import os
from cmu_graphics import cmu_graphics
from cmu_graphics import utils
### ZIPFILE VERSION ###
from cmu_graphics.libs import cairo_loader as cairo
from cmu_graphics.libs import pil_image_loader as Image
### END ZIPFILE VERSION ###

from cmu_graphics.libs import webrequest
from io import BytesIO
import array
import sys
import traceback
import atexit
import subprocess
import json
import unicodedata
import uuid
import re

# start_translate
TRANSLATED_COLOR_NAMES = {'keys': ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornsilk', 'cornflowerblue', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'], 'es': {'aliceblue': 'azulalica', 'antiquewhite': 'blancoantiguo', 'aqua': 'agua', 'aquamarine': 'aguamarina', 'azure': 'azur', 'beige': 'beige', 'bisque': 'bisque', 'black': 'negro', 'blanchedalmond': 'almendrablanqueada', 'blue': 'azul', 'blueviolet': 'azulvioleta', 'brown': 'marrón', 'burlywood': 'madera', 'cadetblue': 'azulcadete', 'chartreuse': 'verdeamarillento', 'chocolate': 'chocolate', 'coral': 'coral', 'cornsilk': 'maizseda', 'cornflowerblue': 'azualaciano', 'crimson': 'carmesí', 'cyan': 'cian', 'darkblue': 'azuloscuro', 'darkcyan': 'cianoscuro', 'darkgoldenrod': 'varilladoradaoscura', 'darkgray': 'grisoscuro', 'darkgreen': 'verdeoscuro', 'darkgrey': 'grisoscuro', 'darkkhaki': 'caquioscuro', 'darkmagenta': 'magentaoscuro', 'darkolivegreen': 'verdeolivaoscuro', 'darkorange': 'naranjaoscuro', 'darkorchid': 'orquídeaoscura', 'darkred': 'rojooscuro', 'darksalmon': 'salmónoscuro', 'darkseagreen': 'marverdeoscuro', 'darkslateblue': 'azulpizarraoscuro', 'darkslategray': 'grispizarraoscuro', 'darkslategrey': 'grispizarraoscuro', 'darkturquoise': 'turquesaoscuro', 'darkviolet': 'violetaoscuro', 'deeppink': 'rosadoprofundo', 'deepskyblue': 'azulcieloprofundo', 'dimgray': 'gristurbio', 'dimgrey': 'gristurbio', 'dodgerblue': 'azulgandul', 'firebrick': 'ladrillo', 'floralwhite': 'blancofloral', 'forestgreen': 'verdebosque', 'fuchsia': 'fucsia', 'gainsboro': 'gainsboro', 'ghostwhite': 'blancofantasma', 'gold': 'oro', 'goldenrod': 'varilladorada', 'gray': 'gris', 'green': 'verde', 'greenyellow': 'verdeamarillo', 'grey': 'gris', 'honeydew': 'melón', 'hotpink': 'rosadofuerte', 'indianred': 'rojoindio', 'indigo': 'índigo', 'ivory': 'marfil', 'khaki': 'caqui', 'lavender': 'lavanda', 'lavenderblush': 'ruborlavanda', 'lawngreen': 'cespedverde', 'lemonchiffon': 'limónchifón', 'lightblue': 'azulclaro', 'lightcoral': 'coralclaro', 'lightcyan': 'cianclaro', 'lightgoldenrodyellow': 'varilladoradaclaraamarilla', 'lightgray': 'grisclaro', 'lightgreen': 'verdeclaro', 'lightgrey': 'grisclaro', 'lightpink': 'rosadoclaro', 'lightsalmon': 'salmónclaro', 'lightseagreen': 'marverdeclaro', 'lightskyblue': 'azulcieloclaro', 'lightslategray': 'grispizarraclaro', 'lightslategrey': 'grispizarraclaro', 'lightsteelblue': 'azulaceroclaro', 'lightyellow': 'amarilloclaro', 'lime': 'lima', 'limegreen': 'limaverde', 'linen': 'lino', 'magenta': 'magenta', 'maroon': 'granate', 'mediumaquamarine': 'aguamarinamedio', 'mediumblue': 'azulmedio', 'mediumorchid': 'orquídeamedio', 'mediumpurple': 'púrpuramedio', 'mediumseagreen': 'marverdemedio', 'mediumslateblue': 'pizarraazulmedio', 'mediumspringgreen': 'verdeprimaveramedio', 'mediumturquoise': 'turquesamedio', 'mediumvioletred': 'violetarojomedio', 'midnightblue': 'azulmedianoche', 'mintcream': 'cremamenta', 'mistyrose': 'nebulosarosa', 'moccasin': 'mocasín', 'navajowhite': 'blanconaranja', 'navy': 'azulmarino', 'oldlace': 'cordónviejo', 'olive': 'oliva', 'olivedrab': 'verdemilitar', 'orange': 'naranja', 'orangered': 'rojonaranja', 'orchid': 'orquídea', 'palegoldenrod': 'varilladoradapálida', 'palegreen': 'verdepálido', 'paleturquoise': 'turquesapálido', 'palevioletred': 'rojovioletapálido', 'papayawhip': 'látigodepapaya', 'peachpuff': 'durazno', 'peru': 'naranjamarrón', 'pink': 'rosado', 'plum': 'ciruela', 'powderblue': 'azulpolvo', 'purple': 'púrpura', 'red': 'rojo', 'rosybrown': 'marrónrosado', 'royalblue': 'azulreal', 'saddlebrown': 'marróncuero', 'salmon': 'salmón', 'sandybrown': 'marrónarenoso', 'seagreen': 'marverde', 'seashell': 'caracol', 'sienna': 'tierra', 'silver': 'plateado', 'skyblue': 'azulcielo', 'slateblue': 'azulpizarra', 'slategray': 'grispizarra', 'slategrey': 'grispizarra', 'snow': 'nieve', 'springgreen': 'verdeprimavera', 'steelblue': 'azulacero', 'tan': 'bronceado', 'teal': 'verdeazulado', 'thistle': 'cardo', 'tomato': 'tomate', 'turquoise': 'turquesa', 'violet': 'violeta', 'wheat': 'trigo', 'white': 'blanco', 'whitesmoke': 'humoblanco', 'yellow': 'amarillo', 'yellowgreen': 'amarilloverde'}, 'de': {'aliceblue': 'aliceblau', 'antiquewhite': 'altweiß', 'aqua': 'wasser', 'aquamarine': 'aquamarin', 'azure': 'azurblau', 'beige': 'beige', 'bisque': 'biskuit', 'black': 'schwarz', 'blanchedalmond': 'bleichemandel', 'blue': 'blau', 'blueviolet': 'blauviolett', 'brown': 'braun', 'burlywood': 'wurzelholz', 'cadetblue': 'kadettenblau', 'chartreuse': 'chartreuse', 'chocolate': 'schokolade', 'coral': 'koralle', 'cornsilk': 'maisseide', 'cornflowerblue': 'kornfeldblau', 'crimson': 'purpur', 'cyan': 'cyan', 'darkblue': 'dunkelblau', 'darkcyan': 'dunkelcyan', 'darkgoldenrod': 'dunkelgoldrute', 'darkgray': 'dunkelgrau', 'darkgreen': 'dunkelgrün', 'darkgrey': 'dunkelgrau', 'darkkhaki': 'dunkelkhaki', 'darkmagenta': 'dunkelmagenta', 'darkolivegreen': 'dunkelolivegrün', 'darkorange': 'dunkelorange', 'darkorchid': 'dunkeorchidee', 'darkred': 'dunkelrot', 'darksalmon': 'dunkellachs', 'darkseagreen': 'dunkelseegrün', 'darkslateblue': 'dunkelschieferblau', 'darkslategray': 'dunkelschiefergrau', 'darkslategrey': 'dunkelschiefergraube', 'darkturquoise': 'dunkeltürkis', 'darkviolet': 'dunkelviolett', 'deeppink': 'dunkelrosa', 'deepskyblue': 'dunkelhimmelblau', 'dimgray': 'mittelgrau', 'dimgrey': 'mittelgraube', 'dodgerblue': 'dodgerblau', 'firebrick': 'backstein', 'floralwhite': 'blütenweiß', 'forestgreen': 'waldgrün', 'fuchsia': 'fuchsie', 'gainsboro': 'gainsboro', 'ghostwhite': 'geisterweiß', 'gold': 'gold', 'goldenrod': 'goldrute', 'gray': 'grau', 'green': 'grün', 'greenyellow': 'grüngelb', 'grey': 'graube', 'honeydew': 'honigtau', 'hotpink': 'kräftigpink', 'indianred': 'indischrot', 'indigo': 'indigo', 'ivory': 'eisen', 'khaki': 'khaki', 'lavender': 'lavendel', 'lavenderblush': 'lavendelröte', 'lawngreen': 'rasengrün', 'lemonchiffon': 'zitronenchiffon', 'lightblue': 'hellblau', 'lightcoral': 'hellkoralle', 'lightcyan': 'hellcyan', 'lightgoldenrodyellow': 'leichtgoldrutengelb', 'lightgray': 'hellgrau', 'lightgreen': 'hellgrün', 'lightgrey': 'hellgraube', 'lightpink': 'hellrosa', 'lightsalmon': 'helllachs', 'lightseagreen': 'hellseegrün', 'lightskyblue': 'hellhimmelblau', 'lightslategray': 'hellschiefergrau', 'lightslategrey': 'hellschiefergraube', 'lightsteelblue': 'hellstahlblau', 'lightyellow': 'hellgelb', 'lime': 'limette', 'limegreen': 'limettengrün', 'linen': 'leinen', 'magenta': 'magenta', 'maroon': 'kastanie', 'mediumaquamarine': 'mittelaquamarine', 'mediumblue': 'mittelblau', 'mediumorchid': 'mittelorchidee', 'mediumpurple': 'mittelviolett', 'mediumseagreen': 'mittelseegrün', 'mediumslateblue': 'mittelschieferblau', 'mediumspringgreen': 'mittelfrühlingsgrün', 'mediumturquoise': 'mitteltürkis', 'mediumvioletred': 'mittelviolettrot', 'midnightblue': 'mitternachtsblau', 'mintcream': 'mintcreme', 'mistyrose': 'nebligrose', 'moccasin': 'mokassin', 'navajowhite': 'navajoweiß', 'navy': 'marineblau', 'oldlace': 'altgold', 'olive': 'olive', 'olivedrab': 'trübolive', 'orange': 'orange', 'orangered': 'orangerot', 'orchid': 'orchidee', 'palegoldenrod': 'blassegoldrute', 'palegreen': 'blassgrün', 'paleturquoise': 'blasstürkis', 'palevioletred': 'blasslilarot', 'papayawhip': 'papayafarben', 'peachpuff': 'pfirsich', 'peru': 'peru', 'pink': 'rosa', 'plum': 'pflaume', 'powderblue': 'taubenblau', 'purple': 'lila', 'red': 'rot', 'rosybrown': 'rostbraun', 'royalblue': 'köningsblau', 'saddlebrown': 'sattelbraun', 'salmon': 'lachs', 'sandybrown': 'sandbraun', 'seagreen': 'seegrün', 'seashell': 'muschel', 'sienna': 'sienna', 'silver': 'silber', 'skyblue': 'himmelblau', 'slateblue': 'schieferblau', 'slategray': 'schiefergrau', 'slategrey': 'schiefergraube', 'snow': 'schneeweiß', 'springgreen': 'frühlingsgrün', 'steelblue': 'stahlblau', 'tan': 'gelbbraun', 'teal': 'petrol', 'thistle': 'diestel', 'tomato': 'tomate', 'turquoise': 'türkis', 'violet': 'violett', 'wheat': 'weizen', 'white': 'weiß', 'whitesmoke': 'weißerrauch', 'yellow': 'gelb', 'yellowgreen': 'gelbgrün'}}
TRANSLATED_GRADIENT_STARTS = {'keys': ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'left-top', 'top', 'right-top', 'left', 'center', 'right', 'left-bottom', 'bottom', 'right-bottom'], 'es': {'top-left': 'superior-izquierda', 'top-right': 'superior-derecha', 'bottom-left': 'inferior-izquierda', 'bottom-right': 'inferior-derecha', 'left-top': 'izquierda-superior', 'top': 'superior', 'right-top': 'derecha-superior', 'left': 'izquierda', 'center': 'centro', 'right': 'derecha', 'left-bottom': 'izquierda-inferior', 'bottom': 'inferior', 'right-bottom': 'derecha-inferior'}, 'de': {'top-left': 'oben-links', 'top-right': 'oben-rechts', 'bottom-left': 'unten-links', 'bottom-right': 'unten-rechts', 'left-top': 'links-oben', 'top': 'oben', 'right-top': 'rechts-oben', 'left': 'links', 'center': 'mitte', 'right': 'rechts', 'left-bottom': 'links-unten', 'bottom': 'unten', 'right-bottom': 'rechts-unten'}}
TRANSLATED_ALIGNS = {'keys': ['left-top', 'top', 'right-top', 'left', 'center', 'right', 'left-bottom', 'bottom', 'right-bottom', 'top-left', 'top-right', 'bottom-left', 'bottom-right'], 'es': {'left-top': 'izquierda-superior', 'top': 'superior', 'right-top': 'derecha-superior', 'left': 'izquierda', 'center': 'centro', 'right': 'derecha', 'left-bottom': 'izquierda-inferior', 'bottom': 'inferior', 'right-bottom': 'derecha-inferior', 'top-left': 'superior-izquierda', 'top-right': 'superior-derecha', 'bottom-left': 'inferior-izquierda', 'bottom-right': 'inferior-derecha'}, 'de': {'left-top': 'links-oben', 'top': 'oben', 'right-top': 'rechts-oben', 'left': 'links', 'center': 'mitte', 'right': 'rechts', 'left-bottom': 'links-unten', 'bottom': 'unten', 'right-bottom': 'rechts-unten', 'top-left': 'oben-links', 'top-right': 'oben-rechts', 'bottom-left': 'unten-links', 'bottom-right': 'unten-rechts'}}
TRANSLATED_SHAPE_ATTRS = {'keys': ['group', 'play', 'pause', 'loop', 'restart', 'remove', 'bold', 'opacity', 'centerX', 'hits', 'borderWidth', 'centerY', 'url', 'left', 'add', 'points', 'startAngle', 'toBack', 'x2', 'y1', 'size', 'initialPoints', 'top', 'align', 'dashes', 'right', 'start', 'y2', 'radius', 'border', 'containsShape', 'background', 'height', 'lineWidth', 'toFront', 'roundness', 'arrowEnd', 'x1', 'fill', 'bottom', 'clear', 'sweepAngle', 'value', 'contains', 'italic', 'visible', 'arrowStart', 'hitsShape', 'font', 'children', 'hitTest', 'width', 'rotateAngle', 'red', 'blue', 'green'], 'es': {'group': 'grupo', 'play': 'toca', 'pause': 'pausa', 'loop': 'repetir', 'restart': 'reiniciar', 'remove': 'quitar', 'bold': 'negrito', 'opacity': 'opacidad', 'centerX': 'centroX', 'hits': 'toca', 'borderWidth': 'anchuraDeBorde', 'centerY': 'centroY', 'url': 'url', 'left': 'izquierda', 'add': 'agregar', 'points': 'puntos', 'startAngle': 'ánguloInicial', 'toBack': 'alFondo', 'x2': 'x2', 'y1': 'y1', 'size': 'tamaño', 'initialPoints': 'puntosIniciales', 'top': 'superior', 'align': 'alinear', 'dashes': 'guión', 'right': 'derecha', 'start': 'inicio', 'colors': 'colores', 'y2': 'y2', 'radius': 'radio', 'border': 'borde', 'containsShape': 'contieneFigura', 'background': 'fondo', 'height': 'altura', 'lineWidth': 'anchuraDeLínea', 'toFront': 'alFrente', 'roundness': 'redondez', 'arrowEnd': 'finalDeFlecha', 'x1': 'x1', 'fill': 'relleno', 'bottom': 'inferior', 'clear': 'vaciar', 'sweepAngle': 'ánguloDeBarrido', 'value': 'valor', 'contains': 'contiene', 'italic': 'itálica', 'visible': 'visible', 'arrowStart': 'inicioDeFlecha', 'hitsShape': 'tocaFigura', 'font': 'fuente', 'children': 'hijos', 'hitTest': 'tocarPrueba', 'width': 'ancho', 'rotateAngle': 'rotarÁngulo', 'red': 'red', 'blue': 'blue', 'green': 'green'}, 'de': {'group': 'gruppe', 'play': 'abspielen', 'pause': 'pausieren', 'loop': 'wiederholen', 'restart': 'neustarten', 'remove': 'entferne', 'bold': 'fett', 'opacity': 'deckkraft', 'centerX': 'mitteX', 'hits': 'trifft', 'borderWidth': 'randBreite', 'centerY': 'mitteY', 'url': 'url', 'left': 'links', 'add': 'fügeHinzu', 'points': 'punkte', 'startAngle': 'anfangsWinkel', 'toBack': 'nachHinten', 'x2': 'x2', 'y1': 'y1', 'size': 'größe', 'initialPoints': 'startPunkte', 'top': 'oben', 'align': 'ausrichtung', 'dashes': 'gestrichelt', 'right': 'rechts', 'start': 'start', 'y2': 'y2', 'radius': 'radius', 'border': 'rand', 'containsShape': 'beinhaltetForm', 'background': 'hintergrund', 'height': 'höhe', 'lineWidth': 'linienBreite', 'toFront': 'nachVorn', 'roundness': 'rundung', 'arrowEnd': 'pfeilEnde', 'x1': 'x1', 'fill': 'füllen', 'bottom': 'unten', 'clear': 'leeren', 'sweepAngle': 'krümmungsWinkel', 'value': 'wert', 'contains': 'beinhaltet', 'italic': 'kursiv', 'visible': 'sichtbar', 'arrowStart': 'pfeilStart', 'hitsShape': 'trifftForm', 'font': 'schriftart', 'children': 'kinder', 'hitTest': 'treffenTest', 'width': 'breite', 'rotateAngle': 'drehWinkel', 'red': 'red', 'blue': 'blue', 'green': 'green'}}
TRANSLATED_BOOLEANS = {'keys': ['True', 'False'], 'es': {'True': 'Verdadero', 'False': 'Falso'}, 'de': {'True': 'Wahr', 'False': 'Falsch'}}
TRANSLATED_GLOBALS = {'keys': ['Arc', 'Circle', 'Group', 'Image', 'Label', 'Line', 'Oval', 'Polygon', 'Rect', 'RegularPolygon', 'Robot', 'Sound', 'Star', 'almostEqual', 'angleTo', 'app', 'assertEqual', 'choice', 'distance', 'fromPythonAngle', 'getPointInDir', 'gradient', 'makeList', 'onKeyHolds', 'onSteps', 'print', 'pythonRound', 'random', 'randrange', 'rgb', 'round', 'rounded', 'seed', 'toPythonAngle', 'onKeyPresses', 'CMUImage'], 'es': {'Arc': 'Arco', 'Circle': 'Círculo', 'Group': 'Grupo', 'Image': 'Imagen', 'Label': 'Rótulo', 'Line': 'Línea', 'Oval': 'Óvalo', 'Polygon': 'Polígono', 'Rect': 'Rect', 'RegularPolygon': 'PolígonoRegular', 'Robot': 'Robot', 'Sound': 'Sonido', 'Star': 'Estrella', 'almostEqual': 'casiIgualA', 'angleTo': 'ánguloA', 'app': 'app', 'assertEqual': 'afirmarIgualdad', 'choice': 'opción', 'distance': 'distancia', 'fromPythonAngle': 'deÁnguloPython', 'getPointInDir': 'obtenerPuntoEnDir', 'gradient': 'gradiente', 'makeList': 'hacerLista', 'onKeyHolds': 'enTeclasRetenidas', 'onSteps': 'enPasos', 'print': 'imprime', 'pythonRound': 'redondearPython', 'random': 'aleatorio', 'randrange': 'rangoAleatorio', 'rgb': 'rgb', 'round': 'redondear', 'rounded': 'redondeado', 'seed': 'semilla', 'toPythonAngle': 'aÁnguloPython', 'onKeyPresses': 'enTeclaPresionadas', 'CMUImage': 'CMUImage'}, 'de': {'Arc': 'Bogen', 'Circle': 'Kreis', 'Group': 'Gruppe', 'Image': 'Bild', 'Label': 'Beschriftung', 'Line': 'Linie', 'Oval': 'Oval', 'Polygon': 'Vieleck', 'Rect': 'Rechteck', 'RegularPolygon': 'RegelmäßigesVieleck', 'Robot': 'Roboter', 'Sound': 'Geräusch', 'Star': 'Stern', 'almostEqual': 'fastGleich', 'angleTo': 'winkelNach', 'app': 'anwendung', 'assertEqual': 'gleichsetzen', 'choice': 'auswahl', 'distance': 'distanz', 'fromPythonAngle': 'vomPythonWinkel', 'getPointInDir': 'erhaltePunktInRichtung', 'gradient': 'farbverlauf', 'makeList': 'macheListe', 'onKeyHolds': 'wennTasteGedrückt', 'onSteps': 'schrittweise', 'print': 'ausgabe', 'pythonRound': 'pythonRunden', 'random': 'zufall', 'randrange': 'zufallsspanne', 'rgb': 'RGB', 'round': 'runden', 'rounded': 'gerundet', 'seed': 'kerne', 'toPythonAngle': 'zumPythonWinkel', 'onKeyPresses': 'wennTasteGedrückt', 'CMUImage': 'CMUImage'}}
TRANSLATED_USER_FUNCTION_NAMES = {'keys': ['onKeyHold', 'onKeyPress', 'onKeyRelease', 'onMouseDrag', 'onMouseMove', 'onMousePress', 'onMouseRelease', 'onStep'], 'es': {'onKeyHold': 'enTeclaRetenida', 'onKeyPress': 'enTeclaPresionada', 'onKeyRelease': 'enTeclaSoltada', 'onMouseDrag': 'enRatónArrastrado', 'onMouseMove': 'enRatónMovido', 'onMousePress': 'enRatónPresionado', 'onMouseRelease': 'enRatónSoltado', 'onStep': 'enPaso'}, 'de': {'onKeyHold': 'beiTasteHalten', 'onKeyPress': 'beiTasteRunter', 'onKeyRelease': 'beiTasteHoch', 'onMouseDrag': 'beiMausMitTasteZiehen', 'onMouseMove': 'beiMausbewegung', 'onMousePress': 'beiMaustasteRunter', 'onMouseRelease': 'beiMaustasteHoch', 'onStep': 'beimSchritt'}}
TRANSLATED_KEY_NAMES = {'keys': ['space', 'enter', 'left', 'right', 'up', 'down', 'pageup', 'pagedown', 'escape', 'delete', 'backspace', 'tab'], 'es': {'space': 'espacio', 'enter': 'intro', 'left': 'izquierda', 'right': 'derecha', 'up': 'arriba', 'down': 'abajo', 'pageup': 'repág', 'pagedown': 'avpág', 'escape': 'escapar', 'delete': 'suprimir', 'backspace': 'retroceso', 'tab': 'pestaña'}, 'de': {'space': 'leertaste', 'enter': 'enter', 'left': 'links', 'right': 'rechts', 'up': 'pfeil-hoch', 'down': 'pfeil-runter', 'pageup': 'bild-hoch', 'pagedown': 'bild-runter', 'escape': 'escape', 'delete': 'entfernen', 'backspace': 'löschen', 'tab': 'tab'}}
TRANSLATED_APP_ATTRS = {'keys': ['background', 'getTextInput', 'group', 'maxShapeCount', 'paused', 'setTextInputs', 'stepsPerSecond', 'stop', 'stopped', 'setMaxShapeCount'], 'es': {'background': 'fondo', 'getTextInput': 'obtenerEntradaDeTexto', 'group': 'grupo', 'maxShapeCount': 'maxCuentaDeFiguras', 'paused': 'pausada', 'setTextInputs': 'establecerEntradaDeTexto', 'stepsPerSecond': 'pasosPorSegundo', 'stop': 'detener', 'stopped': 'detenido', 'setMaxShapeCount': 'establecerCuentaFormasMaximas'}, 'de': {'background': 'hintergrund', 'getTextInput': 'holeTextEingabe', 'group': 'gruppe', 'maxShapeCount': 'maximaleFormMenge', 'paused': 'pausiert', 'setTextInputs': 'setzeTextEingaben', 'stepsPerSecond': 'schritteProSekunde', 'stop': 'stop', 'stopped': 'gestoppt', 'setMaxShapeCount': 'setzeMaxFormAnzahl'}}
TRANSLATED_STRINGS = {'keys': ['Arc', 'Circle', 'Group', 'Image', 'Label', 'Line', 'Oval', 'Polygon', 'Rect', 'RegularPolygon', 'Robot', 'Sound', 'Star', 'almostEqual', 'angleTo', 'app', 'assertEqual', 'choice', 'distance', 'fromPythonAngle', 'getPointInDir', 'gradient', 'makeList', 'onKeyHolds', 'onSteps', 'print', 'pythonRound', 'random', 'randrange', 'rgb', 'round', 'rounded', 'seed', 'toPythonAngle', 'onKeyPresses', 'Arc', 'Circle', 'Group', 'Image', 'Label', 'Line', 'Oval', 'Polygon', 'Rect', 'RegularPolygon', 'Robot', 'Sound', 'Star', 'almostEqual', 'angleTo', 'app', 'assertEqual', 'choice', 'distance', 'fromPythonAngle', 'getPointInDir', 'gradient', 'makeList', 'onKeyHolds', 'onSteps', 'print', 'pythonRound', 'random', 'randrange', 'rgb', 'round', 'rounded', 'seed', 'toPythonAngle', 'onKeyPresses', 'remove', 'bold', 'opacity', 'centerX', 'hits', 'borderWidth', 'centerY', 'url', 'left', 'add', 'points', 'startAngle', 'toBack', 'x2', 'y1', 'size', 'initialPoints', 'top', 'align', 'dashes', 'right', 'start', 'y2', 'radius', 'border', 'containsShape', 'background', 'height', 'lineWidth', 'toFront', 'roundness', 'arrowEnd', 'x1', 'fill', 'bottom', 'clear', 'sweepAngle', 'value', 'contains', 'italic', 'visible', 'arrowStart', 'hitsShape', 'font', 'children', 'hitTest', 'width', 'rotateAngle', '"{{align}}" is not a valid Polygon constructor argument', '"{{attr}}" is not a valid shape constructor argument', '**** Error in onError()!!! ****', 'An assertEqual() statement in a test case failed. See the Console for details.', 'An error occurred. Here is the stack trace:', 'App', 'App.group is readonly', 'App.stopped is readonly', 'Arc', 'Arg Count Error: {{callSpec}}() takes {{argNamesLen}} arguments ({{argNames}}), not {{argsLen}}', 'Arguments to setTextInputs must be strings. %r is not a string.', 'Autograder: error executing solution code!', 'Autograder: error executing user code!', 'Autograding is taking a long time. Your code may have an infinite loop.', 'Both rows and cols must be >= 0', "Cannot set Image's url", "Cannot set Label's height", "Cannot set Label's width", "Cannot set Line's border", "Cannot set Line's borderWidth", 'Circle', 'Circle{{attrs}}', 'Failed to get text input', 'Failed to load image data', 'Font not found: {{baseFontName}}\n', 'Group', 'Group()', 'Group.add(shape)', 'Group.remove(shape)', 'Group.{{attr}} cannot be read or modified', "Group.{{attr}} has no value because its children don't all have the same value for {{attr}}", '{{error}}: Illegal gradient start ({{start}})', 'Image', 'Image{{args}}', 'Internal error (no solution shapes!).  Please try again.', 'Label', 'Label({{args}})', 'Line', 'Line{{args}}', 'Must have an even number of x,y values in initialPoints list', 'Need to pass at least 2 colors to gradient(); you gave {{colorsLength}}', 'No activeDrawing for new Shape', 'No such attribute: {{attr}}', 'None', 'Oval', 'Oval{{args}}', 'Polygon', 'Polygon{{args}}', 'Recording Starts In', 'Rect', 'Rect{{args}}', 'RegularPolygon', 'RegularPolygon{{args}}', 'Robot', 'Shape', 'Shape()', 'Shapes drawn in wrong order', "Sorry, you cannot use Python's input function in CMU CS Academy", 'Sound', 'Sound "{{soundSource}}" failed to play. Disabling it.', 'Star', 'Star{{args}}', 'The loop argument to Sound.play must be True or False, got {{loopRepr}}', 'The restart argument to Sound.play must be True or False, got {{restartRepr}}', 'Too many shapes: Your code created more than {{maxShapeCount}} shapes. If you would like to increase this limit even though it may cause your code to run slowly, call app.setMaxShapeCount(n).', 'Traceback (most recent call last):', '{{error}}: None cannot be used inside gradient.colors', '{{error}}: {{callSpec}} should be {{typeName}} (but {{value}} is of type {{valueType}})', '{{error}}: {{color}} cannot be used inside gradient.colors', '{{error}}: {{callSpec}} should be a color, and {{value}} is not a legal color name', 'Undefined poster in new _CmuGraphics', 'Unknown message {{cmd}}', "Use our rounded(n) instead of Python 3's round(n)\n  Python 3's round(n) does not work as one might expect!\n  If you still want Python 3's round, use pythonRound", 'Wait for fonts to load before using them', 'Wrong # of points ({{userPtsLen}} should be {{solnPtsLen}})', 'You are missing {{missingCount}} shape(s)', "You can't change the size of this group because {{shape}} can't be resized", "You can't get or set the align property", 'You have {{extraCount}} extra shape(s)', 'Your code appeared to be in an infinite loop, so it was terminated.', '\nWarning: Your code created labels with more than\n  1,000 total characters of text. This may cause your\n  program to run very slowly.\n', 'addPoint', 'add{{xy}}', 'align', 'app.background should not be {{userBackgroundString}}', 'app.setMaxShapeCount(n)', 'arrowEnd', 'arrowStart', 'at line', 'background', 'black', 'bold', 'border', 'borderWidth', 'bottom', 'bottom-left', 'bottom-right', 'center', 'centerX', 'centerY', 'centroidX', 'centroidY', 'color', 'containsShape(targetShape)', 'dashes', 'fill', 'font', 'gradient({{colors}}, start={{start}})', 'height', 'hits(x, y)', 'hitsShape(targetShape)', 'initialPoints', 'initialPoints (x value)', 'initialPoints (y value)', 'integer', 'italic', 'keys must be a list', 'left', 'left-bottom', 'left-top', 'line', 'lineWidth', 'list', 'n', 'non-negative-number', 'number', 'number-greater-than-2', 'number-in-range-{{lo}}-{{hi}}', 'opacity', 'oval size', 'points', 'positive-number', 'radius', 'rgb({{r}}, {{g}}, {{b}})', 'right', 'right-bottom', 'right-top', 'rotate.cx', 'rotate.cy', 'rotate.degrees', 'rotateAngle', 'roundness', 'scale{{xy}}', 'shape', 'size', 'startAngle', 'string', 'sweepAngle', 'targetShape', 'top', 'top-left', 'top-right', 'url', 'value', 'visible', 'width', 'x', 'x1', 'x2', 'y', 'y1', 'y2', '{{actual}} != {{expected}}', '{{attr}} in {{object}}', '{{attr}} should not be {{value}}', '{{ordinalName}} point mismatch at {{location}}', 'play', 'pause', 'restart', 'loop', 'TypeError', '{{error}}: in {{callSpec}}, {{value}} is not a legal align value', "{{error}}: {{callSpec}} got an unexpected keyword argument '{{arg}}'", 'contains(x, y)', 'hitTest(x, y)', 'addPoint(x, y)', 'red', 'green', 'blue', '{{callSpec}} must start with http:// or https://'], 'es': {'Arc': 'Arco', 'Circle': 'Círculo', 'Group': 'Grupo', 'Image': 'Imagen', 'Label': 'Rótulo', 'Line': 'Línea', 'Oval': 'Óvalo', 'Polygon': 'Polígono', 'Rect': 'Rect', 'RegularPolygon': 'PolígonoRegular', 'Robot': 'Robot', 'Sound': 'Sonido', 'Star': 'Estrella', 'almostEqual': 'casiIgualA', 'angleTo': 'ánguloA', 'app': 'app', 'assertEqual': 'afirmarIgualdad', 'choice': 'opción', 'distance': 'distancia', 'fromPythonAngle': 'deÁnguloPython', 'getPointInDir': 'obtenerPuntoEnDir', 'gradient': 'gradiente', 'makeList': 'hacerLista', 'onKeyHolds': 'enTeclasRetenidas', 'onSteps': 'enPasos', 'print': 'imprime', 'pythonRound': 'redondearPython', 'random': 'aleatorio', 'randrange': 'rangoAleatorio', 'rgb': 'rgb', 'round': 'redondear', 'rounded': 'redondeado', 'seed': 'semilla', 'toPythonAngle': 'aÁnguloPython', 'onKeyPresses': 'enTeclaPresionadas', 'remove': 'quitar', 'bold': 'negrito', 'opacity': 'opacidad', 'centerX': 'centroX', 'hits': 'toca', 'borderWidth': 'anchuraDeBorde', 'centerY': 'centroY', 'url': 'url', 'left': 'izquierda', 'add': 'agregar', 'points': 'puntos', 'startAngle': 'ánguloInicial', 'toBack': 'alFondo', 'x2': 'x2', 'y1': 'y1', 'size': 'tamaño', 'initialPoints': 'puntosIniciales', 'top': 'superior', 'align': 'alinear', 'dashes': 'guión', 'right': 'derecha', 'start': 'inicio', 'colors': 'colores', 'y2': 'y2', 'radius': 'radio', 'border': 'borde', 'containsShape': 'contieneFigura', 'background': 'fondo', 'height': 'altura', 'lineWidth': 'anchuraDeLínea', 'toFront': 'alFrente', 'roundness': 'redondez', 'arrowEnd': 'finalDeFlecha', 'x1': 'x1', 'fill': 'relleno', 'bottom': 'inferior', 'clear': 'vaciar', 'sweepAngle': 'ánguloDeBarrido', 'value': 'valor', 'contains': 'contiene', 'italic': 'itálica', 'visible': 'visible', 'arrowStart': 'inicioDeFlecha', 'hitsShape': 'tocaFigura', 'font': 'fuente', 'children': 'hijos', 'hitTest': 'tocarPrueba', 'width': 'ancho', 'rotateAngle': 'rotarÁngulo', '"{{align}}" is not a valid Polygon constructor argument': '"alinear" no es un argumento de constructor de Polígono válido', '"{{attr}}" is not a valid shape constructor argument': '"{{attr}}" no es un argumento de constructor de formas válido', '**** Error in onError()!!! ****': '**** ¡¡¡Error dentro de enError()!!! ****', 'An assertEqual() statement in a test case failed. See the Console for details.': 'Una sentencia assertEqual() dentro de un caso de prueba falló. Mire la consola para detalles.', 'An error occurred. Here is the stack trace:': 'Ocurrió un error. Aquí está el seguimiento de la pila:', 'App': 'App', 'App.group is readonly': 'App.grupo es sólo lectura', 'App.stopped is readonly': 'App.detenido es sólo lectura', 'Arg Count Error: {{callSpec}}() takes {{argNamesLen}} arguments ({{argNames}}), not {{argsLen}}': 'Arg Count Error: {{callSpec}}() toma {{argNamesLen}} argumentos ({{argNames}}), no {{argsLen}}', 'Arguments to setTextInputs must be strings. %r is not a string.': 'Arguments to setTextInputs must be strings. %r is not a string.', 'Autograder: error executing solution code!': 'Evaluador: ¡error al ejecutar el código de la solución!', 'Autograder: error executing user code!': 'Evaluador: ¡error al ejecutar el código del usuario!', 'Autograding is taking a long time. Your code may have an infinite loop.': 'El evaluador está tardando mucho. Su código puede tener un bucle infinito.', 'Both rows and cols must be >= 0': 'Ambos las filas y las cols deben ser >= 0', "Cannot set Image's url": 'No se puede establecer el url de una Imagen', "Cannot set Label's height": 'No se puede establecer la altura de una Línea', "Cannot set Label's width": 'No se puede establecer la anchura de una Línea', "Cannot set Line's border": 'No se puede establecer el borde de una Línea', "Cannot set Line's borderWidth": 'No se puede establecer la anchura de una Línea', 'Circle{{attrs}}': 'Círculo{{attrs}}', 'Failed to get text input': 'No se pudo obtener entrade de texto', 'Failed to load image data': 'No se puedo cargar los datos de la imagen', 'Font not found: {{baseFontName}}\n': 'Fuente no encontrada: {{baseFontName}}\\n', 'Group()': 'Grupo()', 'Group.add(shape)': 'Grupo.agregar(figura)', 'Group.remove(shape)': 'Grupo.quitar(figura)', 'Group.{{attr}} cannot be read or modified': 'Grupo.{{attr}} no se puede leer ni modificar', "Group.{{attr}} has no value because its children don't all have the same value for {{attr}}": 'Grupo.{{attr}} no tiene valor porque no todos sus elementos secundarios tienen el mismo valor para {{attr}}', '{{error}}: Illegal gradient start ({{start}})': '{{error}}: Inicio de gradiente ilegal ({{start}})', 'Image{{args}}': 'Imagen{{args}}', 'Internal error (no solution shapes!).  Please try again.': 'Error internal (¡no figuras en su solución!).  Por favor inténtelo otra vez.', 'Label({{args}})': 'Rótulo({{args}})', 'Line{{args}}': 'Línea{{args}}', 'Must have an even number of x,y values in initialPoints list': 'Debe tener un número par de valores x,y dentro de la lista puntosIniciales', 'Need to pass at least 2 colors to gradient(); you gave {{colorsLength}}': 'Necesita dar al menos 2 colores a gradiente(); diste {{colorsLength}}', 'No activeDrawing for new Shape': 'No hay un dibujoActivo para la Figura nueva', 'No such attribute: {{attr}}': 'No existe tal atributo: {{attr}}', 'None': 'None', 'Oval{{args}}': 'Óvalo{{args}}', 'Polygon{{args}}': 'Polígono{{args}}', 'Recording Starts In': 'Grabación comenzando en', 'Rect{{args}}': 'Rect{{args}}', 'RegularPolygon{{args}}': 'PolígonoRegular{{args}}', 'Shape': 'Figura', 'Shape()': 'Figura()', 'Shapes drawn in wrong order': 'Figuras dibujadas en el orden equivocado', "Sorry, you cannot use Python's input function in CMU CS Academy": 'Lo lamento, no puede usar la función de entrada de Python en CMU CS Academy', 'Sound "{{soundSource}}" failed to play. Disabling it.': 'Sonido "{{soundSource}}" no pudo jugar. Desactivando.', 'Star{{args}}': 'Estrella{{args}}', 'The loop argument to Sound.play must be True or False, got {{loopRepr}}': 'El argumento de repetición de Sonido.tocar debe ser Verdadero o Falso, obtuvo {{loopRepr}}', 'The restart argument to Sound.play must be True or False, got {{restartRepr}}': 'El argumento de reinicio de Sonido.tocar debe ser Verdadero o Falso, obtuvo {{reiniciarRepr}}', 'Too many shapes: Your code created more than {{maxShapeCount}} shapes. If you would like to increase this limit even though it may cause your code to run slowly, call app.setMaxShapeCount(n).': 'Demasiadas formas: Su código creó más de {{maxShapeCount}} formas. Si desea aumentar este límite, aunque puede hacer que su código se ejecute lentamente, llame a app.establecerCuentaFormasMaximas(n).', 'Traceback (most recent call last):': 'rastreo (última llamada más reciente):', '{{error}}: None cannot be used inside gradient.colors': '{{error}}: None no se puede usar dentro de gradientes.colores', '{{error}}: {{callSpec}} should be {{typeName}} (but {{value}} is of type {{valueType}})': '{{error}}: {{callSpec}} debe ser {{typeName}} (pero {{value}} es de tipo {{valueType}})', '{{error}}: {{color}} cannot be used inside gradient.colors': '{{error}}: {{color}} no se puede utilizar dentro de gradiente.colores', '{{error}}: {{callSpec}} should be a color, and {{value}} is not a legal color name': '{{error}}: {{callSpec}} debe ser un color, y {{value}} no es un nombre de color legal', 'Undefined poster in new _CmuGraphics': 'Posteador indefinido en nuevo _CmuGraphics', 'Unknown message {{cmd}}': 'Mensaje desconocido {{cmd}}', "Use our rounded(n) instead of Python 3's round(n)\n  Python 3's round(n) does not work as one might expect!\n  If you still want Python 3's round, use pythonRound": 'Use nuestra función redondear(n) en lugar del "round(n)" de Python\\n ¡La función "round(n)" de Python 3 no funciona como uno espera!\\n Si todavía quiere usar el "round" de Python, use "pythonRound"', 'Wait for fonts to load before using them': 'Espere a que se carguen las fuentes antes de usarlas', 'Wrong # of points ({{userPtsLen}} should be {{solnPtsLen}})': '# incorrecto de puntos ({{userPtsLen}} debe ser {{solnPtsLen}})', 'You are missing {{missingCount}} shape(s)': 'Te faltan {{missingCount}} forma(s)', "You can't change the size of this group because {{shape}} can't be resized": 'No puedes cambiar el tamaño de este grupo porque no se puede cambiar el tamaño de {{shape}}', "You can't get or set the align property": 'No puede obtener o establecer la propiedad de alinear', 'You have {{extraCount}} extra shape(s)': 'Tienes {{extraCount}} forma(s) adicionales', 'Your code appeared to be in an infinite loop, so it was terminated.': 'Your code appeared to be in an infinite loop, so it was terminated.', '\nWarning: Your code created labels with more than\n  1,000 total characters of text. This may cause your\n  program to run very slowly.\n': '\\nAdvertencia: Su código creó rótulos con más de\\n  1,000 caracteres de texto en total. Esto puede hacer que su\\n programa se ejecute muy lentamente.\\n', 'addPoint': 'agregarPunto', 'add{{xy}}': 'añadir{{xy}}', 'app.background should not be {{userBackgroundString}}': 'app.fondo no debe ser {{userBackgroundString}}', 'app.setMaxShapeCount(n)': 'app.establecerMáximaCuentaDeFiguras(n)', 'at line': 'en la línea', 'black': 'negro', 'bottom-left': 'inferior-izquierda', 'bottom-right': 'inferior-derecha', 'center': 'centro', 'centroidX': 'centroideX', 'centroidY': 'centroideY', 'color': 'color', 'containsShape(targetShape)': 'contieneFigura(figuraObjetivo)', 'gradient({{colors}}, start={{start}})': 'gradient({{colors}}, start={{start}})', 'hits(x, y)': 'toca(x, y)', 'hitsShape(targetShape)': 'tocaFigura(figuraObjetivo)', 'initialPoints (x value)': 'puntosIniciales (valor x)', 'initialPoints (y value)': 'puntosIniciales (valor y)', 'integer': 'número entero', 'keys must be a list': 'teclas debe ser una lista', 'left-bottom': 'izquierda-inferior', 'left-top': 'izquierda-superior', 'line': 'línea', 'list': 'lista', 'n': 'n', 'non-negative-number': 'número-no-negativo', 'number': 'número', 'number-greater-than-2': 'número-mayor-que-2', 'number-in-range-{{lo}}-{{hi}}': 'número-en-rango-{{lo}}-{{hi}}', 'oval size': 'tamaño de óvalo', 'positive-number': 'número-positivo', 'rgb({{r}}, {{g}}, {{b}})': 'rgb({{r}}, {{g}}, {{b}})', 'right-bottom': 'derecha-inferior', 'right-top': 'derecha-superior', 'rotate.cx': 'rotar.cx', 'rotate.cy': 'rotar.cy', 'rotate.degrees': 'rotar.grados', 'scale{{xy}}': 'escala{{xy}}', 'shape': 'figura', 'string': 'cadena', 'targetShape': 'figuraObjetivo', 'top-left': 'superior-izquierda', 'top-right': 'superior-derecha', 'x': 'x', 'y': 'y', '{{actual}} != {{expected}}': '{{actual}} != {{expected}}', '{{attr}} in {{object}}': '{{attr}} dentro de {{object}}', '{{attr}} should not be {{value}}': '{{attr}} no debe ser {{value}}', '{{ordinalName}} point mismatch at {{location}}': '{{ordinalName}} desajuste de puntos en {{location}}', 'play': 'toca', 'pause': 'pausa', 'restart': 'reiniciar', 'loop': 'repetir', 'TypeError': 'Error de tipo', '{{error}}: in {{callSpec}}, {{value}} is not a legal align value': '{{error}}: en {{callSpec}}, {{value}} no es un valor legal de alineación', "{{error}}: {{callSpec}} got an unexpected keyword argument '{{arg}}'": "{{error}}: {{callSpec}} tiene un argumento de palabra clave inesperado '{{arg}}'", 'contains(x, y)': 'contiene(x, y)', 'hitTest(x, y)': 'tocarPrueba(x, y)', 'addPoint(x, y)': 'agregarPunto(x, y)', 'red': 'red', 'green': 'green', 'blue': 'blue', '{{callSpec}} must start with http:// or https://': '{{callSpec}} debe comenzar con http:// o https://', "Cannot modify attribute '{{attr}}' of '{{className}}' object": "No se puede modificar el atributo '{{attr}}' del objeto de '{{className}}'"}, 'de': {'Arc': 'Bogen', 'Circle': 'Kreis', 'Group': 'Gruppe', 'Image': 'Bild', 'Label': 'Beschriftung', 'Line': 'Linie', 'Oval': 'Oval', 'Polygon': 'Vieleck', 'Rect': 'Rechteck', 'RegularPolygon': 'RegelmäßigesVieleck', 'Robot': 'Roboter', 'Sound': 'Geräusch', 'Star': 'Stern', 'almostEqual': 'fastGleich', 'angleTo': 'winkelNach', 'app': 'anwendung', 'assertEqual': 'gleichsetzen', 'choice': 'auswahl', 'distance': 'distanz', 'fromPythonAngle': 'vomPythonWinkel', 'getPointInDir': 'erhaltePunktInRichtung', 'gradient': 'farbverlauf', 'makeList': 'macheListe', 'onKeyHolds': 'wennTasteGedrückt', 'onSteps': 'schrittweise', 'print': 'ausgabe', 'pythonRound': 'pythonRunden', 'random': 'zufall', 'randrange': 'zufallsspanne', 'rgb': 'RGB', 'round': 'runden', 'rounded': 'gerundet', 'seed': 'kerne', 'toPythonAngle': 'zumPythonWinkel', 'onKeyPresses': 'wennTasteGedrückt', 'remove': 'entferne', 'bold': 'fett', 'opacity': 'deckkraft', 'centerX': 'mitteX', 'hits': 'trifft', 'borderWidth': 'randBreite', 'centerY': 'mitteY', 'url': 'url', 'left': 'links', 'add': 'fügeHinzu', 'points': 'punkte', 'startAngle': 'anfangsWinkel', 'toBack': 'nachHinten', 'x2': 'x2', 'y1': 'y1', 'size': 'größe', 'initialPoints': 'startPunkte', 'top': 'oben', 'align': 'ausrichtung', 'dashes': 'gestrichelt', 'right': 'rechts', 'start': 'start', 'y2': 'y2', 'radius': 'radius', 'border': 'rand', 'containsShape': 'beinhaltetForm', 'background': 'hintergrund', 'height': 'höhe', 'lineWidth': 'linienBreite', 'toFront': 'nachVorn', 'roundness': 'rundung', 'arrowEnd': 'pfeilEnde', 'x1': 'x1', 'fill': 'füllen', 'bottom': 'unten', 'clear': 'leeren', 'sweepAngle': 'krümmungsWinkel', 'value': 'wert', 'contains': 'beinhaltet', 'italic': 'kursiv', 'visible': 'sichtbar', 'arrowStart': 'pfeilStart', 'hitsShape': 'trifftForm', 'font': 'schriftart', 'children': 'kinder', 'hitTest': 'treffenTest', 'width': 'breite', 'rotateAngle': 'drehWinkel', '"{{align}}" is not a valid Polygon constructor argument': '"alinear" ist kein gültiges Argument für den Konstruktor von Polygon',  '"{{attr}}" is not a valid shape constructor argument': '"{{attr}}" ist kein valides Argument des Konstruktors von Form', '**** Error in onError()!!! ****': '**** Fehler in wennFehler()!!! ****', 'An assertEqual() statement in a test case failed. See the Console for details.': 'Eine assertEqual() Anweisung in einem Testfall ist fehlgeschlagen. Schau auf die Konsole um Details zu sehen.', 'An error occurred. Here is the stack trace:': 'Ein unbekannter Fehler ist aufgetreten. Hier ist der Stack Tracke:', 'App': 'Anwendung', 'App.group is readonly': 'App.gruppe nur lesbar', 'App.stopped is readonly': 'App.gestoppt ist nur lesbar', 'Arg Count Error: {{callSpec}}() takes {{argNamesLen}} arguments ({{argNames}}), not {{argsLen}}': 'Fehlerhafte Anzahl der Argumente: {{callSpec}} () akzeptiert {{argNamesLen}} Argumente ({{argNames}}), nicht {{argsLen}}', 'Arguments to setTextInputs must be strings. %r is not a string.': 'Arguments to setTextInputs must be strings. %r is not a string.', 'Autograder: error executing solution code!': 'Autograder: Fehler beim Ausführen des Lösungscodes!', 'Autograder: error executing user code!': 'Autograder: Fehler beim Ausführen des Benutzercodes!', 'Autograding is taking a long time. Your code may have an infinite loop.': 'Autograding dauert lange. Möglicherweise gibt es eine Endlosschleife in deinem Code.', 'Both rows and cols must be >= 0': 'Sowohl Zeilen als auch Spalten müssen >= 0 sein', "Cannot set Image's url": 'Die URL des Bildes kann nicht festgelegt werden', "Cannot set Label's height": 'Die Höhe des Labels kann nicht eingestellt werden', "Cannot set Label's width": 'Breite des Labels kann nicht gesetzt werden', "Cannot set Line's border": 'Der Linienrand kann nicht festgelegt werden', "Cannot set Line's borderWidth": 'Die Rahmenbreite von Line kann nicht festgelegt werden', 'Circle{{attrs}}': 'Kreis{{attrs}}', 'Failed to get text input': 'Fehler bei der Texteingabe', 'Failed to load image data': 'Fehler beim Laden der Bilddaten', 'Font not found: {{baseFontName}}\n': 'Schriftart nicht gefunden: {{baseFontName}}\\n', 'Group()': 'Gruppe()', 'Group.add(shape)': 'Gruppe.fügeHinzu(form)', 'Group.remove(shape)': 'Gruppe.entferne(form)', 'Group.{{attr}} cannot be read or modified': 'Gruppe.{{attr}} kann nicht gelesen oder geändert werden', "Group.{{attr}} has no value because its children don't all have the same value for {{attr}}": 'Gruppe.{{attr}} hat keinen Wert, da die untergeordneten Elemente nicht alle den gleichen Wert für {{attr}} haben', '{{error}}: Illegal gradient start ({{start}})': '{{error}}: Illegaler Start des Farbverlaufs ({{start}})', 'Image{{args}}': 'Bild{{args}}', 'Internal error (no solution shapes!).  Please try again.': 'Interner Fehler (keine Lösungsformen!). Bitte versuche es noche einmal.', 'Label({{args}})': 'Beschriftung({{args}})', 'Line{{args}}': 'Linie{{args}}', 'Must have an even number of x,y values in initialPoints list': 'Muss eine gerade Anzahl von x,y Werten in der Liste anfangsPunkte haben', 'Need to pass at least 2 colors to gradient(); you gave {{colorsLength}}': 'Es müssen mindestens 2 Farben an farbverlauf() übergeben werden. Du hast {{farbenLänge}} gegeben', 'No activeDrawing for new Shape': 'Keine aktiveZeichnung für neue Form', 'No such attribute: {{attr}}': 'Kein solches Attribut: {{attr}}', 'None': 'None', 'Oval{{args}}': 'Oval{{args}}', 'Polygon{{args}}': 'Polygon{{args}}', 'Recording Starts In': 'Aufnahme startet in', 'Rect{{args}}': 'Rechteck{{args}}', 'RegularPolygon{{args}}': 'RegularPolygon {{args}}', 'Shape': 'Form', 'Shape()': 'Form()', 'Shapes drawn in wrong order': 'Formen werden in der falschen Reihenfolge gezeichnet', "Sorry, you cannot use Python's input function in CMU CS Academy": "Leider kannst du Python's input Funktion nicht in CMU CS Academy nutzen", 'Sound "{{soundSource}}" failed to play. Disabling it.': 'Klang "{{soundSource}}" konnte nicht abgespielt werden. Wird deaktiviert.', 'Star{{args}}': 'Stern{{args}}', 'The loop argument to Sound.play must be True or False, got {{loopRepr}}': 'Das Schleifenargument für Sound.play muss True oder False sein, {{loopRepr}}', 'The restart argument to Sound.play must be True or False, got {{restartRepr}}': 'Das Argument um Sound.play neuzustarten muss True oder False sein und {{restartRepr}} erhalten haben', 'Too many shapes: Your code created more than {{maxShapeCount}} shapes. If you would like to increase this limit even though it may cause your code to run slowly, call app.setMaxShapeCount(n).': 'Zu viele Formen:  Ihr Code hat mehr als {{maxShapeCount}} Formen erstellt. Wenn Sie dieses Limit erhöhen möchten, obwohl Ihr Code dadurch möglicherweise langsam ausgeführt wird, rufen Sie app.setzeMaxFormAnzahl(n) auf.', 'Traceback (most recent call last):': 'Aufrufliste (jüngster Aufruf zuletzt)', '{{error}}: None cannot be used inside gradient.colors': '{{error}}: None kann nicht innerhalb von farbverlauf.farben verwendet werden', '{{error}}: {{callSpec}} should be {{typeName}} (but {{value}} is of type {{valueType}})': '{{error}}: {{callSpec}} sollte {{typeName}} sein (aber {{value}} ist vom Typ {{valueType}})', '{{error}}: {{color}} cannot be used inside gradient.colors': '{{error}}: {{color}} kann nicht in gradient.colors verwendet werden', '{{error}}: {{callSpec}} should be a color, and {{value}} is not a legal color name': '{{error}}: {{callSpec}} sollte eine Farbe sein, und {{value}} ist kein zulässiger Farbname', 'Undefined poster in new _CmuGraphics': 'Nicht definiertes Poster in neuem _CmuGraphics', 'Unknown message {{cmd}}': 'Unbekannte Nachricht {{cmd}}', "Use our rounded(n) instead of Python 3's round(n)\n  Python 3's round(n) does not work as one might expect!\n  If you still want Python 3's round, use pythonRound": "Verwenden Sie unsere Funktion rounded(n) anstelle der Python 3 Funktion round(n)\\n Python 3's round(n) funktioniert nicht wie erwartet!\\n Wenn Sie die Funktion round() von Python 3 weiterhin verwenden möchten, dann nutzen Sie pythonRound", 'Wait for fonts to load before using them': 'Warte, bis Zeichensatz geladen ist, bevor du ihn verwendest', 'Wrong # of points ({{userPtsLen}} should be {{solnPtsLen}})': 'Falsche Anzahl von Punkten ({{userPtsLen}} sollte ${{solnPtsLen}} sein)', 'You are missing {{missingCount}} shape(s)': 'Ihnen fehlen {{missingCount}} Form(en)', "You can't change the size of this group because {{shape}} can't be resized": 'Sie können die Größe dieser Gruppe nicht ändern, da die Größe von {{form}} nicht geändert werden kann', "You can't get or set the align property": 'Sie können die Align-Eigenschaft nicht abrufen oder festlegen', 'You have {{extraCount}} extra shape(s)': 'Du hast {{extraCount}} zusätzliche Form(en)', 'Your code appeared to be in an infinite loop, so it was terminated.': 'Your code appeared to be in an infinite loop, so it was terminated.', '\nWarning: Your code created labels with more than\n  1,000 total characters of text. This may cause your\n  program to run very slowly.\n': '\\nWarnung: Ihr Code hat Beschriftungen mit insgesamt mehr als\\n 1.000 Textzeichen erstellt. Dies kann dazu führen, dass Ihr\\n Programm sehr langsam ausgeführt wird.\\n', 'addPoint': 'fügePunktHinzu', 'add{{xy}}': 'addiere{{xy}}', 'app.background should not be {{userBackgroundString}}': 'anwendung.hintergrund sollte nicht {{userBackgroundString}} sein', 'app.setMaxShapeCount(n)': 'anwendung.setzeMaxFormAnzahl(n)', 'at line': 'in Zeile', 'black': 'schwarz', 'bottom-left': 'unten-links', 'bottom-right': 'unten-rechts', 'center': 'mitte', 'centroidX': 'mittelpunktX', 'centroidY': 'mittelpunktY', 'color': 'Farbe', 'containsShape(targetShape)': 'beinhaltetForm(zielForm)', 'gradient({{colors}}, start={{start}})': 'gradient({{colors}}, start={{start}})', 'hits(x, y)': 'trifft(x,y)', 'hitsShape(targetShape)': 'trifftForm(zielForm)', 'initialPoints (x value)': 'anfangsPunkte (x wert)', 'initialPoints (y value)': 'anfangsPunkte (y wert)', 'integer': 'Integer', 'keys must be a list': 'Schlüssel müssen eine Liste sein', 'left-bottom': 'links-unten', 'left-top': 'links-oben', 'line': 'Linie', 'list': 'Liste', 'n': 'n', 'non-negative-number': 'Nicht-negative Zahl', 'number': 'Nummer', 'number-greater-than-2': 'Zahl-größer-als-2', 'number-in-range-{{lo}}-{{hi}}': 'Aufnahme startet in', 'oval size': 'Größe Oval', 'positive-number': 'Positive Zahl', 'rgb({{r}}, {{g}}, {{b}})': 'RGB({{r}}, {{g}}, {{b}})', 'right-bottom': 'rechts-unten', 'right-top': 'rechts-oben', 'rotate.cx': 'drehung.cx', 'rotate.cy': 'drehung.cy', 'rotate.degrees': 'drehung.winkel', 'scale{{xy}}': 'skaliere{{xy}}', 'shape': 'Form', 'string': 'string', 'targetShape': 'zielForm', 'top-left': 'oben-links', 'top-right': 'oben-rechts', 'x': 'x', 'y': 'y', '{{actual}} != {{expected}}': '{{aktuell}}! = {{erwartet}}', '{{attr}} in {{object}}': '{{attr}} in {{object}}', '{{attr}} should not be {{value}}': '{{attr}} sollte nicht {{value}} sein', '{{ordinalName}} point mismatch at {{location}}': '{{ordinalName}} Punkt stimmt nicht mit {{location}} überein', 'play': 'abspielen', 'pause': 'pausieren', 'restart': 'neustarten', 'loop': 'wiederholen', 'TypeError': 'Typfehler', '{{error}}: in {{callSpec}}, {{value}} is not a legal align value': '{{error}}: in {{callSpec}}, {{value}} is not a legal align value', "{{error}}: {{callSpec}} got an unexpected keyword argument '{{arg}}'": "{{error}}: {{callSpec}} got an unexpected keyword argument '{{arg}}'", 'contains(x, y)': 'beinhaltet(x, y)', 'hitTest(x, y)': 'treffenTest(x, y)', 'addPoint(x, y)': 'fügePunktHinzu(x, y)', 'red': 'red', 'green': 'green', 'blue': 'blue', '{{callSpec}} must start with http:// or https://': '{{callSpec}} muss mit http:// or https:// beginnen'}}

# end_translate

cmuGraphicsLanguage = 'en'

def deburr(s):
    return re.sub('[\u0300-\u036f]', '', unicodedata.normalize('NFD', s))

def accentCombinations(word):
    if word == '':
        return ['']

    output = []
    partials = accentCombinations(word[1:])

    letter = word[0]
    deburredLetter = deburr(letter)

    for partial in partials:
        output.append(letter + partial)
        if letter != deburredLetter:
            output.append(deburredLetter + partial)

    return output

def reverseTranslationDict(d):
    reverseDict = dict()
    for language in d:
        if language != 'keys':
            reverseDict[language] = dict()
            for key in d[language]:
                for accentCombination in accentCombinations(d[language][key]):
                    reverseDict[language][accentCombination] = key

    reverseDict['en'] = dict()
    for key in d['keys']:
        reverseDict['en'][key] = key

    return reverseDict

REVERSE_TRANSLATED_COLOR_NAMES = reverseTranslationDict(
  TRANSLATED_COLOR_NAMES
)
REVERSE_TRANSLATED_GRADIENT_STARTS = reverseTranslationDict(
  TRANSLATED_GRADIENT_STARTS
)
REVERSE_TRANSLATED_ALIGNS = reverseTranslationDict(TRANSLATED_ALIGNS);
REVERSE_TRANSLATED_SHAPE_ATTRS = reverseTranslationDict(
  TRANSLATED_SHAPE_ATTRS
)
REVERSE_TRANSLATED_BOOLEANS = reverseTranslationDict(TRANSLATED_BOOLEANS);
REVERSE_TRANSLATED_GLOBALS = reverseTranslationDict(TRANSLATED_GLOBALS);
REVERSE_TRANSLATED_USER_FUNCTION_NAMES = reverseTranslationDict(
  TRANSLATED_USER_FUNCTION_NAMES
)
REVERSE_TRANSLATED_KEY_NAMES = reverseTranslationDict(
  TRANSLATED_KEY_NAMES
)
REVERSE_TRANSLATED_APP_ATTRS = reverseTranslationDict(
  TRANSLATED_APP_ATTRS
)
REVERSE_TRANSLATED_STRINGS = reverseTranslationDict(TRANSLATED_STRINGS);

for language in TRANSLATED_USER_FUNCTION_NAMES:
    if language == 'keys': continue
    for (en_name, trans_name) in TRANSLATED_USER_FUNCTION_NAMES[language].items():
        TRANSLATED_USER_FUNCTION_NAMES[language][en_name] = accentCombinations(trans_name)

TRANSLATION_CONTEXT_LOOKUP = {
  'shape-attr': REVERSE_TRANSLATED_SHAPE_ATTRS,
  'align': REVERSE_TRANSLATED_ALIGNS,
  'gradient-start': REVERSE_TRANSLATED_GRADIENT_STARTS,
  'color': REVERSE_TRANSLATED_COLOR_NAMES,
  'boolean': REVERSE_TRANSLATED_BOOLEANS,
  'global': REVERSE_TRANSLATED_GLOBALS,
  'user-function-name': REVERSE_TRANSLATED_USER_FUNCTION_NAMES,
  'key-name': REVERSE_TRANSLATED_KEY_NAMES,
  'app-attr': REVERSE_TRANSLATED_APP_ATTRS,
}

def getOrDefault(d, key):
    if d is not None and key in d:
        return d[key]
    return key

def reverseSearchLanguageDict(d, key):
    if key in d[cmuGraphicsLanguage]:
        return d[cmuGraphicsLanguage][key], cmuGraphicsLanguage

    for language in d:
        if language != cmuGraphicsLanguage and key in d[language]:
            return d[language][key], language

    return key, None

def t(key, variables = None, language = None):
    if language is None:
        language = cmuGraphicsLanguage

    res = getOrDefault(TRANSLATED_STRINGS.get(language), key)

    if variables is not None:
        for v in variables:
            res = res.replace('{{%s}}' % v, str(variables[v]))

    return res

def toEnglish(key, context, returnLanguage = False):
    if context == 'color':
        key = key.lower()

    searchDict = TRANSLATION_CONTEXT_LOOKUP.get(context, None)
    if searchDict is None:
        searchDict = REVERSE_TRANSLATED_STRINGS

    translation, originalLanguage = reverseSearchLanguageDict(searchDict, key)

    if returnLanguage:
        return translation, originalLanguage
    else:
        return translation

supportedLanguages = ['en', 'es', 'de']

class CMUException(Exception): pass

def printTraceback(exceptionType, exception, tb):
    atexit.unregister(cmu_graphics.check_for_exit_without_run)

    stack = traceback.extract_tb(tb)
    lines = (''.join(traceback.format_list(stack))).splitlines()

    print('An error occurred. Here is the stack trace:')
    hasSourceLines = False

    while (lines):
        try:
            line = lines.pop(0)
            if ', in ' in line:
                line = line[:line.index(', in ')]
            lineNumberLineParts = line.split()
            module = lineNumberLineParts[1]
            lineNumber = int(lineNumberLineParts[-1])
            if (lines and lines[0].startswith('    ')):
                codeLine = lines.pop(0)

            if not (('loop()' in codeLine)
                or ('cmu_graphics.py' in module)
                or ('shape_logic.py' in module)
                or ('cmu_cs3_graphics.py' in module)):

                print('  %s line %d:\n    %s' % (module, lineNumber, codeLine))
        except:
            pass

    # Remove 'shape_logic.' from the name of any exceptions being printed
    if exceptionType != CMUException:
        print(exceptionType.__name__ + ': ' + str(exception))
    else:
        print('Exception: ' + str(exception))

import __main__
if 'CMU_GRAPHICS_DEBUG' not in __main__.__dict__:
    sys.excepthook = printTraceback

def printFullTracebacks():
    sys.excepthook = sys.__excepthook__

def pyThrow(err): raise CMUException(err)

def typeError(obj, attr, value, typeName, isFn):
    if isFn:
        callSpec = t('{{attr}} in {{object}}', { 'attr': t(attr), 'object': t(obj) })
    else:
        if isinstance(obj, str):
            callSpec = '{className}.{attr}'.format(className=t(obj), attr=t(attr))
        else:
            callSpec = '{className}.{attr}'.format(className=t(obj.__class__.__name__), attr=t(attr))
    valueType = type(value).__name__
    err = t(
        '{{error}}: {{callSpec}} should be {{typeName}} (but {{value}} is of type {{valueType}})',
        {'error': t('TypeError'), 'callSpec': callSpec, 'typeName': typeName, 'value': repr(value), 'valueType': valueType}
    )
    pyThrow(err)

def checkArgCount(clsName, fnName, argNames, args):
    if (len(argNames) != len(args)):
        if (clsName and fnName):
            callSpec = '{clsName}.{fnName}'.format(clsName=clsName, fnName=fnName)
        else:
            callSpec = (clsName or fnName)
        pyThrow(t(
            'Arg Count Error: {{callSpec}}() takes {{argNamesLen}} arguments ({{argNames}}), not {{argsLen}}',
            {
                'callSpec': callSpec,
                'argNamesLen': len(argNames),
                'argNames': ",".join(map(t, argNames)),
                'argsLen': len(args)
            }
        ))

def checkInt(obj, attr, value, isFn):
    if type(value) != int: typeError(obj, attr, value, t('integer'), isFn)

def checkNumber(obj, attr, value, isFn):
    if type(value) != int and type(value) != float:
        typeError(obj, attr, value, t('number'), isFn)

def checkPositive(obj, attr, value, isFn):
    checkNumber(obj, attr, value, isFn);
    if (value <= 0): typeError(obj, attr, value, t('positive-number'), isFn)

def checkNonNegative(obj, attr, value, isFn):
    checkNumber(obj, attr, value, isFn)
    if (value < 0): typeError(obj, attr, value, t('non-negative number'), isFn)

def checkRange(obj, attr, value, lo, hi, isFn):
    if ((value < lo) or (value > hi)): typeError(obj, attr, value, t('number-in-range-{{lo}}-{{hi}}', {'lo': lo, 'hi': hi}), isFn)

def checkValue(obj, attr, value, isFn): pass

def checkIntInRange(obj, attr, value, lo, hi, isFn):
    checkInt(obj, attr, value, isFn)
    checkRange(obj, attr, value, lo, hi, isFn)

def checkNumberInRange(obj, attr, value, lo, hi, isFn):
    checkNumber(obj, attr, value, isFn)
    checkRange(obj, attr, value, lo, hi, isFn)

def checkNumberIn0To100(obj, attr, value, isFn):
    checkNumberInRange(obj, attr, value, 0, 100, isFn)

def checkShape(obj, attr, value, isFn):
    if not isinstance(value, Shape):
        typeError(obj, attr, value, t('Shape'), isFn)

def checkWidthHeight(obj, attr, value, isFn):
    if (isinstance(obj, Rect)
        or isinstance(obj, Oval)
        or isinstance(obj, PolygonInCircle)):

        return checkPositive(obj, attr, value, isFn)
    return checkNonNegative(obj, attr, value, isFn)

def checkColor(obj, attr, value, isFn):
    if value == None: return
    if isinstance(value, RGB): return
    if isinstance(value, Gradient): return
    if not isinstance(value, str):
        typeError(obj, attr, value, t('color'), isFn)

    if toEnglish(value, 'color').lower() in CSS3_COLORS_TO_RGB:
        return

    objName = obj if isinstance(obj, str) else obj.__class__.__name__
    pyThrow(
        t(
            '{{error}}: {{callSpec}} should be a color, and {{value}} is not a legal color name',
            {'error': t('TypeError'), 'callSpec': f'{t(objName)}.{t(attr)}', 'value': value}
        )
    )

def checkBoolean(obj, attr, value, isFn):
    if type(value) != bool: typeError(obj, attr, value, 'bool', isFn)

def checkArray(obj, attr, value, isFn):
    if type(value) != list and type(value) != tuple: typeError(obj, attr, value, t('list'), isFn)

def checkString(obj, attr, value, isFn):
    if type(value) != str: typeError(obj, attr, value, 'string', isFn)

def checkUrl(obj, attr, value, isFn):
    if type(value) != str and not isinstance(value, PILWrapper):
        typeError(obj, attr, value, 'string-or-CMUImage', isFn)

def checkBooleanOrArray(obj, attr, value, isFn):
    if type(value) != list and type(value) != tuple: checkBoolean(obj, attr, value, isFn)

def checkAlign(obj, attr, value, isFn):
    if value == None: return # None is a legal align
    if not toEnglish(value, 'align') in aligns:
        pyThrow(t('{{error}}: in {{callSpec}}, {{value}} is not a legal align value', {
            'error': t("TypeError"),
            'callSpec': f'{t(obj.__class__.__name__)}.{t(attr)}',
            'value': value
        }))

def checkNumPoints(obj, attr, value, isFn):
    checkInt(obj, attr, value, isFn)
    if (value < 3): typeError(obj, attr, value, 'number-greater-than-2', isFn)

def checkRoundness(obj, attr, value, isFn):
    if (value is None): return # None is a legal roundness
    checkNumberIn0To100(obj, attr, value, isFn)

def checkSweepAngle(obj, attr, value, isFn):
    checkNumberInRange(obj, attr, value, 0, 360, isFn)

def checkPoint(obj, attr, value, isFn):
    if not isinstance(value, list): typeError(obj, attr, value, 'list', isFn)
    if len(value) != 2: typeError(obj, attr, value, 'point (list of length 2)', isFn)
    checkNumber(obj, attr, value[0], isFn)
    checkNumber(obj, attr, value[1], isFn)

def checkPointList(obj, attr, value, isFn):
    if not isinstance(value, list): typeError(obj, attr, value, 'list', isFn)
    for point in value:
        checkPoint(obj, attr, point, isFn)

def toColorObject(v):
    if not v: return t('None')
    if isinstance(v, str): return CSS3_COLORS_TO_RGB[toEnglish(v, 'color').lower()] or v
    if isinstance(v, RGB) or isinstance(v, Gradient): return v
    raise Exception('toColorObject: unknown color type: {t}'.format(t=type(v)))

def RGBAlmostEqual(v1, v2, epsilon = None):
    if epsilon == None: epsilon = 2
    colorPairs = [[v1.red, v2.red], [v1.green, v2.green], [v1.blue, v2.blue]]
    return all(abs(pair[0] - pair[1]) <= epsilon for pair in colorPairs)

def RGBListAlmostEqual(v1, v2, epsilon):
    if len(v1) != len(v2): return False
    for i in range(len(v1)):
        if type(v1[i]) != type(v2[i]): return False
        if isinstance(v1[i], RGB):
            if not RGBAlmostEqual(v1[i], v2[i], epsilon): return False
        elif isinstance(v1[i], list) or isinstance(v[i], tuple):
            if not RGBListAlmostEqual(v1[i], v2[i], epsilon): return False
        else:
            raise Exception('RGBListAlmostEqual: invalid type: {t}'.format(t=v1[i]))
    return True

def reflectGradientStart(start):
    def toggle(s, a, b):
        if a in s and b in s: raise Exception('Illegal start format: {s}'.format(s=s))
        return s.replace(a, b) if a in s else s.replace(b, a)
    return toggle(toggle(start, 'top', 'bottom'), 'left', 'right')

def colorTest(v1, v2, epsilon):
    v1 = toColorObject(v1)
    v2 = toColorObject(v2)
    if (type(v1) != type(v2)): return 0
    if isinstance(v1, RGB): return 1 if RGBAlmostEqual(v1, v2, epsilon) else 0
    if isinstance(v1, Gradient):
        start1 = canonicalizeGradientStart(v1.start)
        start2 = canonicalizeGradientStart(v2.start)
        if (start1 != start2 and start1 != reflectGradientStart(start2)): return 0
        colors2 = v2.getRGBColors()
        if (start1 != start2):
            colors2.reverse()
        return 1 if RGBListAlmostEqual(v1.getRGBColors(), colors2, epsilon) else 0
    return 1 if v1 == v2 else 0

def eqTest(v1, v2):
    if isinstance(v1, int) or isinstance(v2, float) or isinstance(v2, int) or isinstance(v2, float):
        return 1 if abs(v1 - v2) < 0.005 else 0
    if (isinstance(v1, list) or isinstance(v1, tuple)) and (isinstance(v2, list) or isinstance(v2, tuple)):
        if len(v1) != len(v2): return 0
        for i in range(len(v1)):
            if (eqTest(v1[i], v2[i]) == 0): return 0
        return 1
    return 1 if v1 == v2 else 0

def opacityTest(v1, v2): return eqTest(v1, v2)

aligns = set(['left-top', 'top', 'right-top',
              'left', 'center', 'right',
              'left-bottom', 'bottom', 'right-bottom',
              'top-left', 'top-right', 'bottom-left', 'bottom-right'])

def getAlignAttrs(align):
    if 'left' in align: xattr = 'left'
    elif 'right' in align: xattr = 'right'
    else: xattr = 'centerX'
    if 'top' in align: yattr = 'top'
    elif 'bottom' in align: yattr = 'bottom'
    else: yattr = 'centerY'
    return [xattr, yattr]

def surfaceFromImage(image):
    image = image.convert('RGBA') # ensure we have the correct number of channels
    a = array.array('B', image.tobytes('raw', 'RGBA'))
    surface = cairo.ImageSurface.create_for_data(a, cairo.FORMAT_ARGB32, image.size[0], image.size[1])
    return surface

class PILWrapper(object):
    def __init__(self, image):
        self.image = image
        self._surface = None
        self.uuid = str(uuid.uuid4())

    def get_surface(self):
        if self._surface is None:
            self._surface = surfaceFromImage(self.image)
        return self._surface

    surface = property(get_surface, None)

def hashReference(reference):
    if isinstance(reference, PILWrapper):
        return reference.uuid
    return hash(reference)

def loadImageFromStringReference(reference):
    if (reference.startswith('http')):
        # reference is a url
        try:
            response = webrequest.get(reference)
            image = Image.open(response)
        except:
            pyThrow(t('Failed to load image data'))
    else:
        # reference is a path
        image = Image.open(reference)
    return PILWrapper(image)

def loadImage(reference):
    if isinstance(reference, PILWrapper):
        image = reference
    else:
        image = loadImageFromStringReference(reference)

    surface = image.surface
    activeDrawing.images[hashReference(reference)] = surface

    return {'width': surface.get_width(), 'height': surface.get_height()}

shapeAttrs = dict()
shapeAttrDefaults = dict()

class ShapeAttr(object):
    def __init__(self, name, typeCheckFn, defaultValue):
        self.name = name
        self.typeCheckFn = typeCheckFn
        self.default = defaultValue
        shapeAttrs[name] = self
        shapeAttrDefaults[name] = defaultValue

def initShapeAttrs():
    ShapeAttr('left', checkNumber, 0)
    ShapeAttr('top', checkNumber, 0)
    ShapeAttr('centerX', checkNumber, 0)
    ShapeAttr('centerY', checkNumber, 0)
    ShapeAttr('right', checkNumber, 0)
    ShapeAttr('bottom', checkNumber, 0)
    ShapeAttr('width', checkWidthHeight, 10)
    ShapeAttr('height', checkWidthHeight, 10)
    ShapeAttr('fill', checkColor, 'black')
    ShapeAttr('border', checkColor, None)
    ShapeAttr('borderWidth', checkNonNegative, 2)
    ShapeAttr('dashes', checkBooleanOrArray, False)
    ShapeAttr('opacity', checkNumberIn0To100, 100)
    ShapeAttr('align', checkAlign, None)
    ShapeAttr('rotateAngle', checkNumber, 0)
    ShapeAttr('radius', checkNonNegative, 5)
    ShapeAttr('points', checkNumPoints, 5)
    ShapeAttr('roundness', checkRoundness, 'default')
    ShapeAttr('x1', checkNumber, 0)
    ShapeAttr('y1', checkNumber, 0)
    ShapeAttr('x2', checkNumber, 10)
    ShapeAttr('y2', checkNumber, 10)
    ShapeAttr('arrowStart', checkBoolean, False)
    ShapeAttr('arrowEnd', checkBoolean, False)
    ShapeAttr('lineWidth', checkPositive, 2)
    ShapeAttr('initialPoints', checkArray, [])
    ShapeAttr('pointList', checkPointList, [])
    ShapeAttr('closed', checkBoolean, True)
    ShapeAttr('startAngle', checkNumber, 0)
    ShapeAttr('sweepAngle', checkSweepAngle, 360)
    ShapeAttr('value', checkValue, '')
    ShapeAttr('font', checkString, 'arial')
    ShapeAttr('size', checkNonNegative, 12)
    ShapeAttr('bold', checkBoolean, False)
    ShapeAttr('italic', checkBoolean, False)
    ShapeAttr('visible', checkBoolean, True)
    ShapeAttr('url', checkUrl, None)
    ShapeAttr('db', checkValue, '')
    ShapeAttr('group', checkValue, None)
initShapeAttrs()

# This metaclass prevents 'cmu_graphics.' from being included in the name
# of the type, when type() is called on a Shape/rgb/gradient instance
class _ShapeMetaclass(type):
    def __repr__(cls):
        return "<class '" + t(cls.__name__) + "'>"

    def __str__(cls):
        return "<class '" + t(cls.__name__) + "'>"

class RGB(object, metaclass=_ShapeMetaclass):
    def __init__(self, red, green, blue):
        self._attrs = {'class': self.__class__.__name__}
        self._red = red
        self._green = green
        self._blue = blue
        self._strVal = f'rgb({self._red}, {self._green}, {self._blue})'

    def __getattr__(self, attr):
        en_attr = toEnglish(attr, 'shape-attr')
        if en_attr in ['red', 'green', 'blue']:
            return self.__dict__['_' + en_attr]
        elif attr[0] == '_':
            return self.__dict__[attr]
        else:
            raise AttributeError(f"'{t('rgb')}' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr[0] == '_':
            if attr[1:] in ['red', 'green', 'blue']:
                checkNumberInRange(self, attr[1:], value, 0, 255, False)
            self.__dict__[attr] = value
        else:
            raise Exception(t("Cannot modify attribute '{{attr}}' of '{{className}}' object", {
                'attr': attr,
                'className': t('rgb')
            }))

    def darker(self):
        k = 0.85
        return RGB(
            round(k * self.red),
            round(k * self.green),
            round(k * self.blue)
        )

    def lighter(self):
        k = 0.85
        return RGB(
            round(255 - k * (255 - self.red)),
            round(255 - k * (255 - self.green)),
            round(255 - k * (255 - self.blue))
        )

    def toString(self): return self._strVal

    def __str__(self): return self._strVal

    def __repr__(self): return self._strVal

    def __eq__(self, other):
        if not isinstance(other, RGB): return False
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

RGB.__name__ = 'rgb'

CSS3_COLORS_TO_RGB = {
    "aliceblue": RGB(240, 248, 255),
    "antiquewhite": RGB(250, 235, 215),
    "aqua": RGB(0, 255, 255),
    "aquamarine": RGB(127, 255, 212),
    "azure": RGB(240, 255, 255),
    "beige": RGB(245, 245, 220),
    "bisque": RGB(255, 228, 196),
    "black": RGB(0, 0, 0),
    "blanchedalmond": RGB(255, 235, 205),
    "blue": RGB(0, 0, 255),
    "blueviolet": RGB(138, 43, 226),
    "brown": RGB(165, 42, 42),
    "burlywood": RGB(222, 184, 135),
    "cadetblue": RGB(95, 158, 160),
    "chartreuse": RGB(127, 255, 0),
    "chocolate": RGB(210, 105, 30),
    "coral": RGB(255, 127, 80),
    "cornsilk": RGB(255, 248, 220),
    "cornflowerblue": RGB(100, 149, 237),
    "crimson": RGB(220, 20, 60),
    "cyan": RGB(0, 255, 255),
    "darkblue": RGB(0, 0, 139),
    "darkcyan": RGB(0, 139, 139),
    "darkgoldenrod": RGB(184, 134, 11),
    "darkgray": RGB(169, 169, 169),
    "darkgreen": RGB(0, 100, 0),
    "darkgrey": RGB(169, 169, 169),
    "darkkhaki": RGB(189, 183, 107),
    "darkmagenta": RGB(139, 0, 139),
    "darkolivegreen": RGB(85, 107, 47),
    "darkorange": RGB(255, 140, 0),
    "darkorchid": RGB(153, 50, 204),
    "darkred": RGB(139, 0, 0),
    "darksalmon": RGB(233, 150, 122),
    "darkseagreen": RGB(143, 188, 143),
    "darkslateblue": RGB(72, 61, 139),
    "darkslategray": RGB(47, 79, 79),
    "darkslategrey": RGB(47, 79, 79),
    "darkturquoise": RGB(0, 206, 209),
    "darkviolet": RGB(148, 0, 211),
    "deeppink": RGB(255, 20, 147),
    "deepskyblue": RGB(0, 191, 255),
    "dimgray": RGB(105, 105, 105),
    "dimgrey": RGB(105, 105, 105),
    "dodgerblue": RGB(30, 144, 255),
    "firebrick": RGB(178, 34, 34),
    "floralwhite": RGB(255, 250, 240),
    "forestgreen": RGB(34, 139, 34),
    "fuchsia": RGB(255, 0, 255),
    "gainsboro": RGB(220, 220, 220),
    "ghostwhite": RGB(248, 248, 255),
    "gold": RGB(255, 215, 0),
    "goldenrod": RGB(218, 165, 32),
    "gray": RGB(128, 128, 128),
    "green": RGB(0, 128, 0),
    "greenyellow": RGB(173, 255, 47),
    "grey": RGB(128, 128, 128),
    "honeydew": RGB(240, 255, 240),
    "hotpink": RGB(255, 105, 180),
    "indianred": RGB(205, 92, 92),
    "indigo": RGB(75, 0, 130),
    "ivory": RGB(255, 255, 240),
    "khaki": RGB(240, 230, 140),
    "lavender": RGB(230, 230, 250),
    "lavenderblush": RGB(255, 240, 245),
    "lawngreen": RGB(124, 252, 0),
    "lemonchiffon": RGB(255, 250, 205),
    "lightblue": RGB(173, 216, 230),
    "lightcoral": RGB(240, 128, 128),
    "lightcyan": RGB(224, 255, 255),
    "lightgoldenrodyellow": RGB(250, 250, 210),
    "lightgray": RGB(211, 211, 211),
    "lightgreen": RGB(144, 238, 144),
    "lightgrey": RGB(211, 211, 211),
    "lightpink": RGB(255, 182, 193),
    "lightsalmon": RGB(255, 160, 122),
    "lightseagreen": RGB(32, 178, 170),
    "lightskyblue": RGB(135, 206, 250),
    "lightslategray": RGB(119, 136, 153),
    "lightslategrey": RGB(119, 136, 153),
    "lightsteelblue": RGB(176, 196, 222),
    "lightyellow": RGB(255, 255, 224),
    "lime": RGB(0, 255, 0),
    "limegreen": RGB(50, 205, 50),
    "linen": RGB(250, 240, 230),
    "magenta": RGB(255, 0, 255),
    "maroon": RGB(128, 0, 0),
    "mediumaquamarine": RGB(102, 205, 170),
    "mediumblue": RGB(0, 0, 205),
    "mediumorchid": RGB(186, 85, 211),
    "mediumpurple": RGB(147, 112, 216),
    "mediumseagreen": RGB(60, 179, 113),
    "mediumslateblue": RGB(123, 104, 238),
    "mediumspringgreen": RGB(0, 250, 154),
    "mediumturquoise": RGB(72, 209, 204),
    "mediumvioletred": RGB(199, 21, 133),
    "midnightblue": RGB(25, 25, 112),
    "mintcream": RGB(245, 255, 250),
    "mistyrose": RGB(255, 228, 225),
    "moccasin": RGB(255, 228, 181),
    "navajowhite": RGB(255, 222, 173),
    "navy": RGB(0, 0, 128),
    "oldlace": RGB(253, 245, 230),
    "olive": RGB(128, 128, 0),
    "olivedrab": RGB(107, 142, 35),
    "orange": RGB(255, 165, 0),
    "orangered": RGB(255, 69, 0),
    "orchid": RGB(218, 112, 214),
    "palegoldenrod": RGB(238, 232, 170),
    "palegreen": RGB(152, 251, 152),
    "paleturquoise": RGB(175, 238, 238),
    "palevioletred": RGB(216, 112, 147),
    "papayawhip": RGB(255, 239, 213),
    "peachpuff": RGB(255, 218, 185),
    "peru": RGB(205, 133, 63),
    "pink": RGB(255, 192, 203),
    "plum": RGB(221, 160, 221),
    "powderblue": RGB(176, 224, 230),
    "purple": RGB(128, 0, 128),
    "red": RGB(255, 0, 0),
    "rosybrown": RGB(188, 143, 143),
    "royalblue": RGB(65, 105, 225),
    "saddlebrown": RGB(139, 69, 19),
    "salmon": RGB(250, 128, 114),
    "sandybrown": RGB(244, 164, 96),
    "seagreen": RGB(46, 139, 87),
    "seashell": RGB(255, 245, 238),
    "sienna": RGB(160, 82, 45),
    "silver": RGB(192, 192, 192),
    "skyblue": RGB(135, 206, 235),
    "slateblue": RGB(106, 90, 205),
    "slategray": RGB(112, 128, 144),
    "slategrey": RGB(112, 128, 144),
    "snow": RGB(255, 250, 250),
    "springgreen": RGB(0, 255, 127),
    "steelblue": RGB(70, 130, 180),
    "tan": RGB(210, 180, 140),
    "teal": RGB(0, 128, 128),
    "thistle": RGB(216, 191, 216),
    "tomato": RGB(255, 99, 71),
    "turquoise": RGB(64, 224, 208),
    "violet": RGB(238, 130, 238),
    "wheat": RGB(245, 222, 179),
    "white": RGB(255, 255, 255),
    "whitesmoke": RGB(245, 245, 245),
    "yellow": RGB(255, 255, 0),
    "yellowgreen": RGB(154, 205, 50),
}

gradientStarts = [ 'left-top',     'top',    'right-top',
                   'left',        'center',    'right',
                   'left-bottom', 'bottom', 'right-bottom' ];

alternateGradientStarts = {
  'top-left': 'left-top',
  'top-right': 'right-top',
  'bottom-left': 'left-bottom',
  'bottom-right': 'right-bottom',
}

def canonicalizeGradientStart(start):
    start = toEnglish(start, 'gradient-start');
    if start in alternateGradientStarts: return alternateGradientStarts[start]
    return start

class Gradient(object, metaclass=_ShapeMetaclass):
    def __init__(self, colors, start):
        checkArray(self, t('colors'), colors, False)
        if len(colors) < 2:
            pyThrow(t('Need to pass at least 2 colors to gradient(); you gave {{colorLen}}', {'colorLen': v1[i]}));
        for color in colors:
            if color is None:
                pyThrow(t('{{error}}: None cannot be used inside gradient.colors', {'error': t('TypeError')}))
            if isinstance(color, Gradient):
                pyThrow(t('{{error}}: {{color}} cannot be used inside gradient.colors', {'color': color, 'error': t('TypeError')}))
            checkColor(self, 'colors', color, False)
        checkString(self, t('start'), start, False)
        if (
            (toEnglish(start, 'gradient-start') not in gradientStarts) and
            (toEnglish(start, 'gradient-start') not in alternateGradientStarts)
        ):
            pyThrow(t('{{error}}: Illegal gradient start ({{start}})', {'error': t('TypeError'), 'start': start}))
        self.attrs = {'class': self.__class__.__name__, 'colors': colors, 'start': start}

    def toString(self):
        colors = ', '.join([repr(c) for c in self.colors])
        return f"{t('gradient')}({colors}, {t('start')}='{t(self.start)}')"

    def getRGBColors(self):
        return list(map(lambda v: v if isinstance(v, RGB) else CSS3_COLORS_TO_RGB[toEnglish(v, 'color').lower()], self.colors))

    def toRGBList(self):
        if (self.start == 'center'):
            return self.getRGBColors()
        return sorted([self.getRGBColors(), reversed(self.getRGBColors())])

    def __getattr__(self, attr):
        en_attr = toEnglish(attr, 'shape-attr')
        if en_attr == 'start':
            if attr == 'start':
                return self.attrs['start']
            return t(self.attrs['start'])
        elif en_attr == 'colors':
            return self.attrs['colors']
        raise AttributeError(f"'{t('gradient')}' object has no attribute '{attr}'")

    def __setattr__(self, attr, val):
        if attr == 'attrs':
            self.__dict__[attr] = val
            return val
        else:
            raise Exception(t("Cannot modify attribute '{{attr}}' of '{{className}}' object", {
                            'attr': attr, 'className': t('gradient')}))

    def __eq__(self, other):
        if not isinstance(other, Gradient):
            return False
        if len(self.colors) != len(other.colors):
            return False
        if canonicalizeGradientStart(self.start) != canonicalizeGradientStart(other.start):
            return False
        for i in range(len(self.colors)):
            c1 = self.colors[i]
            c2 = other.colors[i]
            if type(c1) != type(c2):
                return False
            if c1 != c2:
                return False
        return True

    def __repr__(self):
        return self.toString()

    def __str__(self):
        return self.toString()

Gradient.__name__ = 'gradient'

class Drawing(object):
    def __init__(self):
        self.tlg = None
        self.images = {}
        self.addCounter = 0
        self.appProperties = {
            'maxShapeCount': 2000
        }
        self.nextShapeId = 0

activeDrawing = Drawing()

'''
 Shape
 ├ Group
 ├ Label
 └ Polygon
    ├ Rect
    ├ Line
    ├ PolygonInCircle
    │ ├ RegularPolygon
    │ └ Star
    └ PolygonWithTransform
      ├ CMUImage
      └ Oval
        ├ Arc
        └ Circle
'''

def shape_property(getter, setter=None):
    def shape_getter(self):
        return utils.truncateIntegerFloats(getter(self))
    return property(shape_getter, setter)

class Shape(object):
    def __init__(self, attrs = None):
        self.id = activeDrawing.nextShapeId
        activeDrawing.nextShapeId += 1

        self._group = self.oldGroup = None
        # A list of shapes that this shape was in front of its current/previous group
        self.shapesToBeInFrontOf = []
        self.shapesInOldGroup = {}
        self.isGroup = False
        # zIndex is global across all groups
        self.zindex = -1
        self.attrs = {'class': self.__class__.__name__}
        if (not attrs is None):
            if 'defaultAlign' in attrs:
                self.defaultAlign = attrs['defaultAlign']
                del attrs['defaultAlign']
            else:
                self.defaultAlign = t('center')
        self.attrDefaults = shapeAttrDefaults
        if (not attrs is None):
            self.set(attrs)
        if (not attrs or not attrs.get('noGroup', False)) and (activeDrawing.tlg is not None):
            activeDrawing.tlg.add(self)

    def get(self, attr):
        if attr in self.attrs: return self.attrs[attr]
        # Translate so the default shape fill is determined by user language
        return t(self.attrDefaults[attr])

    def setAttr(self, attr, value):
        self.attrs[attr] = value
        return value

    def set(self, attrs):
        result = None
        for attr in attrs:
            value = attrs[attr]
            attrSpec = shapeAttrs.get(attr, None)
            if attrSpec is not None:
                attrSpec.typeCheckFn(self, attr, value, False)
            result = self.setAttr(attr, value)
            # TODO: Handle labels
        return result

    def get_group(self): return self._group
    def set_group(self, v): pyThrow(t("You can't set the group property"))
    group = shape_property(get_group, set_group)

    def get_align(self): pyThrow(t("You can't get or set the align property"))
    def set_align(self, v): pyThrow(t("You can't get or set the align property"))
    align = shape_property(get_align, set_align)

    def get_doNotInspect(self): return self.attrs.get('doNotInspect', None)
    def set_doNotInspect(self, v): self.attrs['doNotInspect'] = v; return v
    doNotInspect = shape_property(get_doNotInspect, set_doNotInspect)

    def get_centerX(self): return self.get('centerX', None)
    def set_centerX(self, v): self.set({'centerX', v}); return v
    centerX = shape_property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY', None)
    def set_centerY(self, v): self.set({'centerY', v}); return v
    centerY = shape_property(get_centerY, set_centerY)

    def get_left(self): return self.centerX - self.width / 2
    def set_left(self, v): self.addx(v - self.left); return v
    left = shape_property(get_left, set_left)

    def get_top(self): return self.centerY - self.height / 2
    def set_top(self, v): self.centerY = v + self.height / 2; return v
    top = shape_property(get_top, set_top)

    def get_right(self): return self.centerX + self.width / 2
    def set_right(self, v): self.centerX = v - self.width / 2; return v
    right = shape_property(get_right, set_right)

    def get_bottom(self): return self.centerY + self.height / 2
    def set_bottom(self, v): self.centerY = v - self.height / 2; return v
    bottom = shape_property(get_bottom, set_bottom)

    def addxy(self, varName = None, d = None):
        if (d == 0): return
        if (varName == 'x'): self.centerX += d
        else: self.centerY += d

    def addx(self, dx): self.addxy('x', dx)
    def addy(self, dy): self.addxy('y', dy)

    def get_centroidX(self): return self.centroid[0]
    def set_centroidX(self, v):
        self.addx(v - self.centroidX)
    centroidX = shape_property(get_centroidX, set_centroidX)

    def get_centroidY(self): return self.centroid[1]
    def set_centroidY(self, v):
        self.addy(v - self.centroidY)
    centroidY = shape_property(get_centroidY, set_centroidY)

    def get_width(self): return self.get('width')
    def set_width(self, v):
        self.scalexy('x', v / self.width)
        self.set({'width': v})
    width = shape_property(get_width, set_width)

    def get_height(self): return self.get('height')
    def set_height(self, v):
        self.scalexy('y', v / self.height)
        self.set({'height': v})
    height = shape_property(get_height, set_height)

    def get_fill(self): return self.get('fill')
    def set_fill(self, v): return self.set({'fill': v})
    fill = shape_property(get_fill, set_fill)
    def get_border(self): return self.get('border')
    def set_border(self, v): return self.set({'border': v})
    border = shape_property(get_border, set_border)
    def get_borderWidth(self): return self.get('borderWidth')
    def set_borderWidth(self, v): return self.set({'borderWidth': v})
    borderWidth = shape_property(get_borderWidth, set_borderWidth)
    def get_dashes(self): return self.get('dashes')
    def set_dashes(self, v): return self.set({'dashes': v})
    dashes = shape_property(get_dashes, set_dashes)
    def get_opacity(self): return self.get('opacity')
    def set_opacity(self, v): return self.set({'opacity': v})
    opacity = shape_property(get_opacity, set_opacity)
    def get_closed(self): return self.get('closed')
    def set_closed(self, v): return self.set({'closed': v})
    closed = shape_property(get_closed, set_closed)
    def get_db(self): return self.get('db')
    def set_db(self, v): return self.set({'db': v})
    db = shape_property(get_db, set_db)

    def get_visible(self):
        return (self._group != None) and (self._group.visible or self._group == activeDrawing.tlg._shape)
    def set_visible(self, v):
        if v == self.visible: return
        if v:
            if self.oldGroup:
                self.oldGroup.insert(self)
            else:
                activeDrawing.tlg.add(self)
        else:
            self._group.remove(self)
    visible = shape_property(get_visible, set_visible)

    def doAlign(self, x, y, v):
        v = toEnglish(v, 'align')
        [xattr, yattr] = getAlignAttrs(v)
        setattr(self, xattr, x)
        setattr(self, yattr, y)

    def get_centroid(self): return [self.centerX, self.centerY]
    def set_centroid(self, v): pyThrow("Centroid cannot be set")
    centroid = shape_property(get_centroid, set_centroid)

    def getRotateAnchor(self): return self.centroid

    def get_rotateAngle(self): return self.get('rotateAngle')
    def set_rotateAngle(self, v): self.rotate(v - self.rotateAngle)
    rotateAngle = shape_property(get_rotateAngle, set_rotateAngle)

    def rotate(self, degrees = None, cx = None, cy = None):
        if (cx is None and cy is None):
            cx, cy = self.getRotateAnchor()
            cx = utils.round6(cx)
            cy = utils.round6(cy)
        self.set({'rotateAngle': self.rotateAngle + degrees})
        self.doRotate(degrees, cx, cy)

    def doRotate(self, degrees, cx, cy):
        pyThrow("Must override doRotate method!")

    def toString(self): return t('Shape()')
    def _toString(self): return self.toString() # so cmu_graphics can access toString

    def contains(self, *arguments): # contains(x,y)
        checkArgCount(self.__class__.__name__, t('contains'), [t('x'), t('y')], arguments)
        x, y = arguments
        checkNumber(t('contains(x, y)'), 'x', x, True)
        checkNumber(t('contains(x, y)'), 'y', y, True)
        return utils.polygonContainsPoint(self.getApproxPoints(), x, y)

    def hits(self, *arguments): # hits(x,y)
        checkArgCount(self.__class__.__name__, t('hits'), [t('x'), t('y')], arguments)
        x, y = arguments
        checkNumber(t('hits(x, y)'), t('x'), x, True)
        checkNumber(t('hits(x, y)'), t('y'), y, True)
        pts = self.getApproxPoints()
        if (not utils.polygonContainsPoint(pts, x, y)): return False
        if (self.fill or isinstance(self, CMUImage)): return True
        border = self.border
        if (not border): return False;
        # ok, so we have a border, but no fill, so we 'hit' if we
        # are within a borderWidth of the border
        bw = self.borderWidth if border else 0
        return utils.pointNearPolygonBorder(pts, x, y, bw)

    def edgesIntersect(self, shape):
        pts1 = self.getApproxPoints()
        pts2 = shape.getApproxPoints()
        k = None
        for i in range(len(pts1)):
            x1, y1 = pts1[i];
            k = (i + 1) % (len(pts1));
            x2, y2 = pts1[k];
            for j in range(len(pts2)):
                x3, y3 = pts2[j];
                k = (j + 1) % (len(pts2))
                x4, y4 = pts2[k];
                if (utils.segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4)):
                    return True
        return False

    def containsShape(self, *arguments):
        checkArgCount(self.__class__.__name__, t('containsShape'), [t('targetShape')], arguments);
        (targetShape,) = arguments
        checkShape(t('containsShape(targetShape)'), t('targetShape'), targetShape, True);

        if (isinstance(targetShape, Group)):
            return all([self.containsShape(shape) for shape in targetShape.children])

        # This shapes fully contains the target shape if their
        # edges do not intersect, but (any point of / all points of)
        # the targetShape are inside this shape
        x = targetShape.centerX
        y = targetShape.centerY
        return (not self.edgesIntersect(targetShape) and self.contains(x, y))

    def getBounds(self):
        return { 'left': self.left, 'top': self.top, 'width': self.width, 'height': self.height }

    def boundsIntersect(self, targetShape, margin = None):
        # Symmetric.  Fast pre-test for hitsShape.  If this is False, hitsShape
        # must be False.  If this is True, hitsShape *may* be True.
        if (margin is None): margin = 0
        b1 = self.getBounds()
        b2 = targetShape.getBounds()
        return ((b1['left'] + margin <= b2['left'] + b2['width']) and
                (b2['left'] + margin <= b1['left'] + b1['width']) and
                (b1['top']  + margin <= b2['top'] + b2['height']) and
                (b2['top']  + margin <= b1['top'] + b1['height']))

    def hitsShape(self, *arguments):
        checkArgCount(self.__class__.__name__, t('hitsShape'), [t('targetShape')], arguments)
        (targetShape,) = arguments
        checkShape(t('hitsShape(targetShape)'), t('targetShape'), targetShape, True)
        # Symmetric.  Two shapes hit each other if any of their
        # vertices hit the other or their edges intersect.
        myShapes = utils.getChildShapes(self)
        targetShapes = utils.getChildShapes(targetShape)

        for i in range(len(myShapes)):
            for j in range(len(targetShapes)):
                if (myShapes[i].edgesIntersect(targetShapes[j])):
                    return True

        for i in range(len(myShapes)):
            for j in range(len(targetShapes)):
                shape1 = myShapes[i]
                shape2 = targetShapes[j]
                if any((shape2.hits(pt[0], pt[1]) for pt in shape1.getApproxPoints())):
                    return True
                if any((shape1.hits(pt[0], pt[1]) for pt in shape2.getApproxPoints())):
                    return True
                if myShapes[i].edgesIntersect(targetShapes[j]):
                    return True

        return False

    def toFront(self):
        if self.group is not None:
            self.group._toFront(self)

    def toBack(self):
        if  self.group is not None:
            self.group._toBack(self)

    def setFillOrStrokeStyle(self, ctx, fillOrBorder):
        style = self.getFillOrStrokeStyle(fillOrBorder)
        if isinstance(style, cairo.Gradient):
            ctx.set_source(style)
        else:
            ctx.set_source_rgba(*style)

    def getFillOrStrokeStyle(self, fillOrBorder):
        if fillOrBorder is None: return (0,0,0,1)
        if isinstance(fillOrBorder, Gradient):
            gradient = fillOrBorder
            g = self.createBaseGradient(gradient)
            n = len(gradient.colors)
            for i in range(n):
                color = gradient.colors[i]
                g.add_color_stop_rgba(i/(n-1), *self.getFillOrStrokeStyle(color))
            return g
        if isinstance(fillOrBorder, str):
            fillOrBorder = CSS3_COLORS_TO_RGB[toEnglish(fillOrBorder, 'color').lower()]
        # Flips RGBA to BGRA because Cairo is going to flip it back
        rgba = (fillOrBorder.blue/255, fillOrBorder.green/255, fillOrBorder.red/255,  self.opacity / 100)
        return rgba

    def setDashes(self, ctx):
        if isinstance(self.dashes, bool):
            ctx.set_dash([5,5] if self.dashes else [])
        else:
            ctx.set_dash(self.dashes)

    def toFront(self):
        if self._group:
            self._group._toFront(self)

    def toBack(self):
        if self._group:
            self._group._toBack(self)

    def drawDbPoint(self, ctx, x, y, color):
        ctx.save()
        color_list = list(self.getFillOrStrokeStyle(color))
        color_list[3] = 1 # ignore our own opacity when drawing db points
        ctx.set_source_rgba(*color_list)
        r = 3
        ctx.new_path()
        ctx.arc(x, y, r, 0, 2 * math.pi)
        ctx.close_path()
        ctx.fill()
        ctx.restore()

    def drawDbCenter(self, ctx):
        self.drawDbPoint(ctx, self.centerX, self.centerY, 'red')

    def drawDbCentroid(self, ctx):
        if isinstance(self, Polygon):
            centroid = utils.getPolygonCentroid(self.pointList)
            self.drawDbPoint(ctx, centroid[0], centroid[1], 'magenta')
        else:
            self.drawDbCenter(ctx)

    def drawDbBox(self, ctx):
        ctx.save()
        ctx.new_path()
        ctx.rectangle(self.left, self.top, self.width, self.height)
        ctx.close_path()
        ctx.set_line_width(2)
        color_list = list(self.getFillOrStrokeStyle('red'))
        color_list[3] = 1 # ignore our own opacity when drawing db points
        ctx.set_source_rgba(*color_list)
        ctx.set_dash([2, 2])
        ctx.stroke()
        ctx.restore()

    def drawDbPoints(self, ctx):
        pts = self.getApproxPoints()
        ctx.save()
        r = 4
        self.setFillOrStrokeStyle(ctx, 'magenta')
        # dots at corners
        for pt in pts:
            x, y = pt
            ctx.new_path()
            ctx.arc(x, y, r, 0, 2 * math.pi)
            ctx.close_path()
            ctx.fill()
        # now connect the dots
        ctx.new_path
        utils.makePolygonPath(pts, ctx)
        ctx.close_path()
        ctx.set_line_width(3)
        self.setFillOrStrokeStyle(ctx, 'magenta')
        ctx.set_dash([7, 7])
        ctx.stroke()
        ctx.restore()

    def draw(self, ctx):
        ctx.save()
        if (self.isGroup):
            for s in self._shapes: s.draw(ctx)
        else:
            bw = self.borderWidth if self.border else 0
            if isinstance(self, Label):
                if str(self.value) != self.valueStr:
                    self.valueStr = str(self.value)
                    self.setDims()
                [targetX, targetY] = self.getApproxPoints()[6] # target start,top of text
                # rotate around targetX, targetY
                if self.rotateAngle != 0:
                    ctx.translate(targetX, targetY)
                    ctx.rotate(utils.toRadians(self.rotateAngle))
                    ctx.translate(-targetX, -targetY)

                ctx.select_font_face(*getFont(self.font, self.bold, self.italic))
                ctx.set_font_size(self.size)
                text = str(self.value)

                ctx.new_path()
                ctx.move_to(targetX - self.attrs['xAdjust'], targetY)

                ctx.text_path(text)

                self.setFillOrStrokeStyle(ctx, self.fill)
                ctx.fill_preserve()
                if bw:
                    self.setFillOrStrokeStyle(ctx, self.border)
                    ctx.set_line_width(bw)
                    ctx.stroke()
            elif isinstance(self, Line):
                if self.fill:
                    ctx.new_path()
                    self.setFillOrStrokeStyle(ctx, self.fill)
                    self.setDashes(ctx)
                    ctx.set_line_width(self.lineWidth)
                    ctx.move_to(self.x1, self.y1)
                    ctx.line_to(self.x2, self.y2)
                    ctx.stroke()

                    self.drawArrows(ctx)
            else:
                self.makePath(ctx)
                if (self.closed): ctx.close_path()
                if (self.fill and len(self.pointList) > 2):
                    self.setFillOrStrokeStyle(ctx, self.fill)
                    ctx.fill_preserve()
                if bw:
                    # (*note) if there is a border, draw with 2x borderWidth,
                    # but clipped to shape so only 1x inner border is drawn
                    bw *= 2
                    ctx.clip_preserve()
                    self.setFillOrStrokeStyle(ctx, self.border)
                    # @TODO
                    self.setDashes(ctx)
                    if isinstance(self, Arc):
                        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
                    ctx.set_line_width(bw)
                    ctx.stroke()
            if isinstance(self, CMUImage):
                self.drawImage(ctx)
            ctx.restore()

            db = self.db
            if db != '' and type(db) == str:
                if db == 'all' or 'points' in db: self.drawDbPoints(ctx)
                if db == 'all' or 'box' in db: self.drawDbBox(ctx)
                if db == 'all' or 'center' in db: self.drawDbCenter(ctx)
                if db == 'all' or 'centroid' in db: self.drawDbCentroid(ctx)

def countShapesInGroup(shape):
    # First make it a sl shape so hasattr doesn't call getattr and crash
    if hasattr(shape, '_shape'):
        shape = shape._shape
    if not hasattr(shape, '_shapes') or not shape._shapes:
        return 1
    return sum(map(countShapesInGroup, shape))

def checkRecursiveGroupAddition(group, shape):
    if shape.isGroup:
        if group.id == shape.id:
            pyThrow(t('Group.add failed: a Group cannot contain itself.'))
        for subshape in shape._shapes:
            checkRecursiveGroupAddition(group, subshape)

class Group(Shape):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.isGroup = True
        self._shapes = []

    def toString(self): return t('Group()')

    def __iter__(self):
        return iter(self.children)

    def get_children(self):
        return list(map(lambda s: s.studentShape, self._shapes))
    children = shape_property(get_children)

    def insert(self, shape, newIndex=None):
        if shape._group:
            shape._group.remove(shape)
        # By default, put this shape at the top of the group
        if newIndex == None:
            newIndex = len(self._shapes)
            # But if it was in this group before, put it back in front of all the
            # shapes that it was in front of before
            if (shape.oldGroup == self):
                newIndex = 0
                for s2 in shape.shapesToBeInFrontOf:
                    s2Index = self._shapes.index(s2) if s2 in self._shapes else -1
                    if (s2Index >= 0):
                        newIndex = max(newIndex, s2Index + 1)

                for (i, s2) in enumerate(self._shapes):
                    if s2.id not in shape.shapesInOldGroup and shape.id > s2.id:
                        newIndex = max(newIndex, i + 1)

        self._shapes.insert(newIndex, shape)
        shape._group = self
        shape.zindex = -1
        shape.oldGroup = None
        shape.shapesToBeInFrontOf = []
        shape.shapesInOldGroup = {}

    def add(self, *shapes):
        for i in range(len(shapes)):
            checkShape(t('Group.add(shape)'), t('shape'), shapes[i], True)
            checkRecursiveGroupAddition(self, shapes[i])
            activeDrawing.addCounter += 1
            if activeDrawing.addCounter % 100 == 0:
                if countShapesInGroup(activeDrawing.tlg) > activeDrawing.appProperties['maxShapeCount']:
                    pyThrow(
                      t(
                        'Too many shapes: Your code created more than {{maxShapeCount}} shapes. If you would like to increase this limit even though it may cause your code to run slowly, call app.setMaxShapeCount(n).',
                        { 'maxShapeCount': str(activeDrawing.appProperties['maxShapeCount']) }
                      )
                    )
            self.insert(shapes[i])

    def _toFront(self, shape):
        self.remove(shape)
        self.insert(shape, len(self._shapes))

    def _toBack(self, shape):
        self.remove(shape)
        self.insert(shape, 0)

    def remove(self, shape):
        checkShape(t('Group.remove(shape)'), t('shape'), shape, True)
        currentIndex = self._shapes.index(shape) if shape in self._shapes else -1
        shape.shapesToBeInFrontOf = self._shapes[:currentIndex]
        shape.shapesInOldGroup = {}

        for s in self._shapes:
            shape.shapesInOldGroup[s.id] = s

        for i in range(currentIndex + 1, len(self._shapes)):
            self._shapes[i].shapesToBeInFrontOf.append(shape)

        if shape in self._shapes: self._shapes.remove(shape)
        shape.oldGroup = self
        shape._group = None
        shape.zindex = -1

        def f(shape):
            if shape.isGroup:
                for s in shape._shapes: f(s)
            else:
                shape.zindex = -1

        f(shape)

    def clear(self):
        shapes = self._shapes
        self._shapes = []
        for shape in shapes: self.remove(shape)

    def hits(self, x, y):
        return self.hitTest(x, y) != None

    def hitTest(self, x, y):
        for i in range(len(self._shapes)-1, -1, -1):
            shape = self._shapes[i]
            if (shape.hits(x, y)):
                return shape.studentShape
        return None

    def contains(self, x, y):
        return any(shape.contains(x, y) for shape in self._shapes)

    def containsShape(self, target):
        return any(shape.containsShape(shape) for shape in self._shapes)

    def addx(self, dx):
        for shape in self._shapes: shape.left += dx
    def get_left(self):
        if len(self._shapes) == 0: return 0
        return min(map(lambda s: s.left, self._shapes))
    def set_left(self, v): self.addx(v - self.left)
    left = shape_property(get_left, set_left)
    def get_right(self):
        if len(self._shapes) == 0: return 0
        return max(map(lambda s: s.right, self._shapes))
    def set_right(self, v): self.addx(v - self.right)
    right = shape_property(get_right, set_right)
    def get_centerX(self): return (self.left + self.right) / 2
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = shape_property(get_centerX, set_centerX)

    def addy(self, dy):
        for shape in self._shapes: shape.top += dy
    def get_top(self):
        if (len(self._shapes) == 0):
            return 0
        return min(map(lambda s: s.top, self._shapes))
    def set_top(self, v): self.addy(v - self.top)
    top = shape_property(get_top, set_top)
    def get_bottom(self):
        if len(self._shapes) == 0: return 0
        return max(map(lambda s: s.bottom, self._shapes))
    def set_bottom(self, v): self.addy(v - self.bottom)
    bottom = shape_property(get_bottom, set_bottom)
    def get_centerY(self): return (self.top + self.bottom) / 2
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = shape_property(get_centerY, set_centerY)

    def scalexy(self, varName, k, scaleAnchor = None):
        if (k == 1): return
        if (scaleAnchor is None):
            scaleAnchor = self.centroid
        for s in self._shapes: s.scalexy(varName, k, scaleAnchor)

    def get_width(self): return self.right - self.left
    def set_width(self, v):
        if self.width == 0:
            self.scaleToTarget('x', v)
        else:
            self.scalexy('x', (v / self.width))
    width = shape_property(get_width, set_width)
    def get_height(self): return self.bottom - self.top
    def set_height(self, v):
        if self.height == 0:
            self.scaleToTarget('y', v)
        else:
            self.scalexy('y', (v / self.height))
    height = shape_property(get_height, set_height)

    def rotate(self, degrees = None, cx = None, cy = None):
        if (len(self._shapes) == 0):
            self.set({'rotateAngle': self.rotateAngle + degrees})
            return

        super().rotate(degrees, cx, cy)

    def doRotate(self, degrees, cx, cy):
        for s in self._shapes: s.rotate(degrees, cx, cy)

    def get_area(self):
        result = 0
        for s in self._shapes: result += s.area
        return result
    area = shape_property(get_area)

    def get_centroid(self):
        x, y, A = 0, 0, 0
        for s in self._shapes:
            c = s.centroid
            a = s.area
            cx, cy = c[0], c[1]
            x += a * cx
            y += a * cy
            A += a
        return [x, y] if A == 0 else [x / A, y / A]
    centroid = shape_property(get_centroid)

    # pass-through attrs (PTA's)

    def getPTA(self, attr):
        val = None
        for shape in self._shapes:
            if val is None:
                val = getattr(shape, attr)
            else:
                if ((attr == 'fill' and not colorTest(getattr(shape, attr), val, 0.005))
                    or (attr == 'opacity' and not opacityTest(getattr(shape, attr), val))):
                    pyThrow(
                        t(
                            "Group.{{attr}} has no value because its children don't all have the same value for {{attr}}",
                            {'attr': t(attr)}
                        )
                    )
        return val

    def setPTA(self, attr, v):
        for shape in self._shapes:
            setattr(shape, attr, v)
        return v

    def get_fill(self): return self.getPTA('fill')
    def set_fill(self, v): return self.setPTA('fill', v)
    fill = shape_property(get_fill, set_fill)
    def get_opacity(self): return self.getPTA('opacity')
    def set_opacity(self, v): return self.setPTA('opacity', v)
    opacity = shape_property(get_opacity, set_opacity)

    def noPTA(self, attr):
        pyThrow(t('Group.{{attr}} cannot be read or modified', { 'attr': t(attr) }))

    def get_border(self): return self.noPTA('border')
    def set_border(self, v): return self.noPTA('border', v)
    border = shape_property(get_border, set_border)
    def get_borderWidth(self): return self.noPTA('borderWidth')
    def set_borderWidth(self, v): return self.noPTA('borderWidth', v)
    borderWidth = shape_property(get_borderWidth, set_borderWidth)
    def get_dashes(self): return self.noPTA('dashes')
    def set_dashes(self, v): return self.noPTA('dashes', v)
    dashes = shape_property(get_dashes, set_dashes)
    def get_arrowEnd(self): return self.noPTA('arrowEnd')
    def set_arrowEnd(self, v): return self.noPTA('arrowEnd', v)
    arrowEnd = shape_property(get_arrowEnd, set_arrowEnd)
    def get_arrowStart(self): return self.noPTA('arrowStart')
    def set_arrowStart(self, v): return self.noPTA('arrowStart', v)
    arrowStart = shape_property(get_arrowStart, set_arrowStart)
    def get_url(self): return self.noPTA('url')
    def set_url(self, v): return self.noPTA('url', v)
    url = shape_property(get_url, set_url)
    def get_radius(self): return self.noPTA('radius')
    def set_radius(self, v): return self.noPTA('radius', v)
    radius = shape_property(get_radius, set_radius)
    def get_points(self): return self.noPTA('points')
    def set_points(self, v): return self.noPTA('points', v)
    points = shape_property(get_points, set_points)
    def get_roundness(self): return self.noPTA('roundness')
    def set_roundness(self, v): return self.noPTA('roundness', v)
    roundness = shape_property(get_roundness, set_roundness)
    def get_x1(self): return self.noPTA('x1')
    def set_x1(self, v): return self.noPTA('x1', v)
    x1 = shape_property(get_x1, set_x1)
    def get_y1(self): return self.noPTA('y1')
    def set_y1(self, v): return self.noPTA('y1', v)
    y1 = shape_property(get_y1, set_y1)
    def get_x2(self): return self.noPTA('x2')
    def set_x2(self, v): return self.noPTA('x2', v)
    x2 = shape_property(get_x2, set_x2)
    def get_y2(self): return self.noPTA('y2')
    def set_y2(self, v): return self.noPTA('y2', v)
    y2 = shape_property(get_y2, set_y2)
    def get_lineWidth(self): return self.noPTA('lineWidth')
    def set_lineWidth(self, v): return self.noPTA('lineWidth', v)
    lineWidth = shape_property(get_lineWidth, set_lineWidth)
    def get_closed(self): return self.noPTA('closed')
    def set_closed(self, v): return self.noPTA('closed', v)
    closed = shape_property(get_closed, set_closed)
    def get_startAngle(self): return self.noPTA('startAngle')
    def set_startAngle(self, v): return self.noPTA('startAngle', v)
    startAngle = shape_property(get_startAngle, set_startAngle)
    def get_sweepAngle(self): return self.noPTA('sweepAngle')
    def set_sweepAngle(self, v): return self.noPTA('sweepAngle', v)
    sweepAngle = shape_property(get_sweepAngle, set_sweepAngle)
    def get_value(self): return self.noPTA('value')
    def set_value(self, v): return self.noPTA('value', v)
    value = shape_property(get_value, set_value)
    def get_font(self): return self.noPTA('font')
    def set_font(self, v): return self.noPTA('font', v)
    font = shape_property(get_font, set_font)
    def get_size(self): return self.noPTA('size')
    def set_size(self, v): return self.noPTA('size', v)
    size = shape_property(get_size, set_size)
    def get_bold(self): return self.noPTA('bold')
    def set_bold(self, v): return self.noPTA('bold', v)
    bold = shape_property(get_bold, set_bold)
    def get_italic(self): return self.noPTA('italic')
    def set_italic(self, v): return self.noPTA('italic', v)
    italic = shape_property(get_italic, set_italic)

    def scaleToTarget(self, varName, target):
        for shape in self._shapes:
            if getattr(shape, 'scaleToTarget'):
                shape.scaleToTarget(varName, target)

fontCtx = cairo.Context(cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0))

def getFont(baseFontName, isBold=False, isItalic=False):
    ok = True
    if 'mono' in baseFontName or 'courier' in baseFontName:
        fontName = 'Courier New'
    elif 'arial' in baseFontName or 'sans' in baseFontName:
        fontName = 'Arial'
    elif baseFontName.lower() in ('serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'):
        fontName = baseFontName.lower()
    else:
        fontName = 'Arial'

    bold = cairo.FONT_WEIGHT_BOLD if isBold else cairo.FONT_WEIGHT_NORMAL
    italic = cairo.FONT_SLANT_ITALIC if isItalic else cairo.FONT_SLANT_NORMAL

    return (fontName, italic, bold)

class Label(Shape):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.valueStr = None
        if attrs is not None:
            self.setDims()

    def getApproxPoints(self): return self.attrs['approxPoints']

    def doRotate(self, degrees, cx, cy):
        newCenter = utils.rotatePoint([self.centerX, self.centerY], degrees, cx, cy)
        self.set({
            'centerX': newCenter[0],
            'centerY': newCenter[1]
        })
        self.setDims()

    def setDims(self):
        fontCtx.save()
        fontCtx.select_font_face(*getFont(self.font, self.bold, self.italic))
        fontCtx.set_font_size(self.size)

        cx = self.attrs['centerX']
        cy = self.attrs['centerY']
        stringValue = utils.convertLabelValue(self.value)
        xBearing, yBearing, width, height, xAdvance, yAdvance = fontCtx.text_extents(stringValue)
        height = -yBearing
        unrotatedWidth = width
        hasOuterSpaces = len(stringValue) > 0 and (stringValue[0] == ' ' or stringValue[-1] == ' ')
        if hasOuterSpaces:
            unrotatedWidth = max(unrotatedWidth, xAdvance)
        #unrotatedHeight = -height
        unrotatedHeight = height
        x0 = cx - unrotatedWidth / 2
        y0 = cy - unrotatedHeight / 2
        x1 = cx + unrotatedWidth / 2
        y1 = cy + unrotatedHeight / 2
        pts = [[x0, y0], [(x0 + x1) / 2, y0], [x1, y0],
               [x1, (y0 + y1) / 2],
               [x1, y1], [(x0 + x1) / 2, y1], [x0, y1],
               [x0, (y0 + y1) / 2]]
        a = self.rotateAngle
        if a: pts = utils.rotatePoints(pts, a, self.centerX, self.centerY)
        self.set({
            'approxPoints': pts,
            'xAdjust': 0 if hasOuterSpaces else xBearing
        })
        box = utils.getBoxDims(pts)
        self.set({
            'width': box['width'],
            'height': box['height']
        })
        fontCtx.restore()

    def get_area(self): return self.width * self.height
    area = shape_property(get_area)

    def createBaseGradient(self, gradient):
        # The approxPoints of a Label are positioned correctly (self.rotateAngle has
        # already been applied to them). However, when we draw the text, we
        # rotate the canvas around the start,bottom point of the text. So, we have to make a
        # gradient that is positioned such that it will be in the correct place after
        # being rotated around start,bottom by self.rotateAngle.
        start = canonicalizeGradientStart(gradient.start)
        [targetX, targetY] = self.getApproxPoints()[6] # target start,top of text
        if (start == 'center'):
            cx = self.centerX;
            cy = self.centerY;
            r = utils.distance(cx, cy, self.right, self.top);
            [[cx, cy]] = utils.rotatePoints([[cx, cy]], -self.rotateAngle, targetX, targetY);
            return cairo.RadialGradient(cx, cy, 0, cx, cy, r);


        startToPointIndex = {
            'left-top': 0,
            'top': 1,
            'right-top': 2,
            'right': 3,
            'right-bottom': 4,
            'bottom': 5,
            'left-bottom': 6,
            'left': 7,
        }

        if (startToPointIndex.get(start) is None):
            pyThrow('Illegal gradient start {start}'.format(start=start))

        [x0, y0] = self.getApproxPoints()[startToPointIndex[start]]
        endIndex = (startToPointIndex[start] + 4) % 8
        [x1, y1] = self.getApproxPoints()[endIndex]

        if (self.rotateAngle != 0):
            [[x0, y0], [x1, y1]] = utils.rotatePoints(
                [[x0, y0], [x1, y1]],
                -self.rotateAngle,
                targetX,
                targetY
            )

        return cairo.LinearGradient(x0, y0, x1, y1)

    def get_width(self): return self.get('width')
    def set_width(self, v): pyThrow(t("Cannot set Label's width"))
    width = shape_property(get_width, set_width)
    def get_height(self): return self.get('height')
    def set_height(self, v): pyThrow(t("Cannot set Label's height"))
    height = shape_property(get_height, set_height)

    def get_centerX(self): return self.get('centerX')
    def set_centerX(self, v):
        self.set({'centerX': v})
        self.setDims()
        return v
    centerX = shape_property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY')
    def set_centerY(self, v):
        self.set({'centerY': v})
        self.setDims()
        return v
    centerY = shape_property(get_centerY, set_centerY)

    def get_value(self): return self.get('value')
    def set_value(self, v):
        self.set({'value': v})
        self.valueStr = str(v)
        self.setDims()
        return v
    value = shape_property(get_value, set_value)
    def get_font(self): return self.get('font')
    def set_font(self, v):
        self.set({'font': v})
        self.setDims()
        return v
    font = shape_property(get_font, set_font)
    def get_size(self): return self.get('size')
    def set_size(self, v):
        self.set({'size': v})
        self.setDims()
        return v
    size = shape_property(get_size, set_size)
    def get_bold(self): return self.get('bold')
    def set_bold(self, v):
        self.set({'bold': v})
        self.setDims()
        return v
    bold = shape_property(get_bold, set_bold)
    def get_italic(self): return self.get('italic')
    def set_italic(self, v):
        self.set({'italic': v})
        self.setDims()
        return v
    italic = shape_property(get_italic, set_italic)

    def toString(self):
        return f"{t('Label')}({self.value}, {self.centerX}, {self.centerY})"

class Polygon(Shape):
    def __init__(self, attrs=None):
        if (not attrs is None and 'initialPoints' in attrs):
            if (len(attrs['initialPoints']) % 2 != 0):
                pyThrow(t('Must have an even number of x,y values in initialPoints list'))
            for i in range(0, len(attrs['initialPoints']), 2):
                x, y = attrs['initialPoints'][i], attrs['initialPoints'][i+1]
                checkNumber(t('Polygon'), t('initialPoints (x value)'), x, False)
                checkNumber(t('Polygon'), t('initialPoints (y value)'), y, False)

        super().__init__(attrs)
        self._cachedCentroid = self._cachedArea = None

        if (not attrs is None and 'initialPoints' in attrs):
            pts = attrs['initialPoints']
            pointList = []
            for i in range(0, len(pts), 2):
                x, y = pts[i], pts[i+1]
                pointList.append([x,y])
            self.pointList = pointList

    def get_pointList(self): return self.get('pointList')
    def set_pointList(self, pl):
        self.set({'pointList': pl})
        self.setDims()
    pointList = shape_property(get_pointList, set_pointList)

    def get_area(self):
        if (self._cachedArea is None):
            self._cachedArea = abs(utils.getPolygonArea(self.pointList))
        return self._cachedArea
    area = shape_property(get_area)

    def get_centroid(self):
        if self._cachedCentroid is None:
            self._cachedCentroid = utils.getPolygonCentroid(self.pointList)
        return self._cachedCentroid
    centroid = shape_property(get_centroid)

    def addPoint(self, x, y):
        checkNumber(t('addPoint'), t('x'), x, False)
        checkNumber(t('addPoint'), t('y'), y, False)
        self.pointList.append([x, y])
        self.pointList = self.pointList # alert to change

    def makePath(self, ctx):
        return utils.makePolygonPath(self.pointList, ctx)

    def setDims(self):
        self._cachedCentroid = self._cachedArea = None
        if len(self.pointList) == 0:
            self.set({
                'centerX': 0,
                'centerY': 0,
                'width': 0,
                'height': 0,
            })
            return
        boxDims = utils.getBoxDims(self.pointList)
        self.set({
            'centerX': boxDims['left'] + boxDims['width'] / 2,
            'centerY': boxDims['top'] + boxDims['height'] / 2,
            'width': boxDims['width'],
            'height': boxDims['height']
        })

    def get_centerX(self): return self.get('centerX')
    def set_centerX(self, v):
        self.addx(v - self.centerX)
        # centerX will get set by setDims(), but we overwrite the value
        # with what the user gave so that there are no rounding errors.
        self.set({'centerX': v})
    centerX = shape_property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY')
    def set_centerY(self, v):
        self.addy(v - self.centerY)
        # centerY will get set by setDims(), but we overwrite the value
        # with what the user gave so that there are no rounding errors.
        self.set({'centerY': v})
    centerY = shape_property(get_centerY, set_centerY)

    def get_left(self): return min(map(lambda point: point[0], self.pointList))
    def set_left(self, v): self.addx(v - self.left); return v
    left = shape_property(get_left, set_left)

    def get_top(self): return min(map(lambda point: point[1], self.pointList))
    def set_top(self, v): self.addy(v - self.top); return v
    top = shape_property(get_top, set_top)

    def get_right(self): return max(map(lambda point: point[0], self.pointList))
    def set_right(self, v): self.addx(v - self.right); return v
    right = shape_property(get_right, set_right)

    def get_bottom(self): return max(map(lambda point: point[1], self.pointList))
    def set_bottom(self, v): self.addy(v - self.bottom); return v
    bottom = shape_property(get_bottom, set_bottom)

    def addxy(self, varName, d):
        if d == 0: return
        varIndex = 0 if varName == 'x' else 1
        pointList = self.pointList
        for i in range(len(pointList)):
            pointList[i][varIndex] += d
        self.pointList = pointList # alert to change

    def scalexy(self, varName, k, scaleAnchor = None):
        if k == 1: return
        varIndex = 0 if varName == 'x' else 1
        pointList = self.pointList
        cxy = (scaleAnchor or self.getScaleAnchor())[varIndex]
        for i in range(len(pointList)):
            dxy = pointList[i][varIndex] - cxy
            pointList[i][varIndex] = cxy + k * dxy
        self.pointList = pointList # alert to change

    def getScaleAnchor(self): return [self.centerX, self.centerY]

    def doRotate(self, degrees, cx, cy):
        self.pointList = utils.rotatePoints(self.pointList, degrees, cx, cy)

    def getApproxPoints(self):
        return self.pointList

    def toString(self):
        args = utils.flatten(self.pointList)
        return t('Polygon{{args}}', {'args': utils.roundedTupleString(args, 2)})

    def createBaseGradient(self, fillOrBorder):
        gradient = fillOrBorder
        start = canonicalizeGradientStart(gradient.start)
        rotateAnchor = self.getRotateAnchor()

        unrotatedPoints = self.pointList
        if self.rotateAngle != 0:
            unrotatedPoints = utils.rotatePoints(
                self.pointList, -self.rotateAngle, rotateAnchor[0], rotateAnchor[1]
            )
        dims = utils.getBoxDims(unrotatedPoints)

        if start == 'center':
            if isinstance(self, Oval):
                r = max(dims['width'], dims['height']) / 2
            else:
                r = utils.distance(
                    dims['left'] + dims['width'] / 2, dims['top'] + dims['height'] / 2,
                    dims['left'], dims['top']
                )

            if isinstance(self, Star):
                r *= 0.8

            return cairo.RadialGradient(
                rotateAnchor[0], rotateAnchor[1], 0,
                rotateAnchor[0], rotateAnchor[1], r,
            )

        left, top = dims['left'], dims['top']
        right = left + dims['width']
        bottom = top + dims['height']
        centerX = left + dims['width'] / 2
        centerY = top + dims['height'] / 2
        if (start == 'left-top'):
            x0 = left; x1 = right; y0 = top; y1 = bottom
        elif (start == 'left'):
            x0 = left; x1 = right; y0 = y1 = centerY
        elif (start == 'left-bottom'):
            x0 = left; x1 = right; y0 = bottom; y1 = top
        elif (start == 'top'):
            x0 = x1 = centerX; y0 = top; y1 = bottom
        elif (start == 'bottom'):
            x0 = x1 = centerX; y0 = bottom; y1 = top
        elif (start == 'right-top'):
            x0 = right; x1 = left; y0 = top; y1 = bottom
        elif (start == 'right'):
            x0 = right; x1 = left; y0 = y1 = centerY
        elif (start == 'right-bottom'):
            x0 = right; x1 = left; y0 = bottom; y1 = top
        else:
            pyThrow('Illegal gradient start ({start})'.format(start=start))

        if self.rotateAngle != 0:
            [[x0, y0], [x1, y1]] = utils.rotatePoints([[x0, y0], [x1, y1]], self.rotateAngle,
                rotateAnchor[0], rotateAnchor[1]
            )

        return cairo.LinearGradient(x0, y0, x1, y1)

class Rect(Polygon):
    def __init__(self, attrs=None):
        if not attrs is None:
            right = attrs['left'] + attrs['width']
            bottom = attrs['top'] + attrs['height']
            attrs['defaultAlign'] = 'left-top'
            attrs['initialPoints'] = [
                attrs['left'], attrs['top'],
                right, attrs['top'],
                right, bottom,
                attrs['left'], bottom,
            ]
        super().__init__(attrs)

    def getScaleAnchor(self): return [self.left, self.top]

    def toString(self):
        args = [self.left, self.top, self.width, self.height]
        return t('Rect{{args}}', {'args': utils.roundedTupleString(args, 2)})

class Line(Polygon):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getLinePoints(attrs['x1'], attrs['y1'], attrs['x2'], attrs['y2'], 2))
        
        exactValues = {
            'x1': attrs['x1'],
            'x2': attrs['x2'],
            'y1': attrs['y1'],
            'y2': attrs['y2'],
        }
        
        del attrs['x1']
        del attrs['y1']
        del attrs['x2']
        del attrs['y2']
        super().__init__(attrs)
        self.exactValues = exactValues;

    def addxy(self, varName, d):
        super().addxy(varName, d)
        attrs = []
        if (varName == 'x'):
            attrs = ['x1', 'x2']
        else:
            attrs = ['y1', 'y2']

        for attr in attrs:
            if (attr in self.exactValues):
                self.exactValues[attr] += d

    def scalexy(self, varName, k, scaleAnchor):
        super().scalexy(varName, k, scaleAnchor)
        self.exactValues = {}

    def rotate(self, degrees = None, cx = None, cy = None):
        super().rotate(degrees, cx, cy)
        self.exactValues = {}

    def getXY(self, i0, i1, j, name):
        if (name in self.exactValues):
            return self.exactValues[name]
    
        points = self.pointList
        return (points[i0][j] + points[i1][j]) / 2

    def setXY(self, i0, i1, j, v, name):
        self.exactValues[name] = v;
        p = self.pointList
        oldv = (p[i0][j] + p[i1][j]) / 2
        dv = v - oldv
        p[i0][j] += dv
        p[i1][j] += dv
        self.pointList = self.pointList; # alert to change
        return v

    def get_x1(self): return self.getXY(0, 3, 0, 'x1') # x1,y1 at points 0 and 3, 0=x
    def set_x1(self, v): return self.setXY(0, 3, 0, v, 'x1') # x1,y1 at points 0 and 3, 0=x
    x1 = shape_property(get_x1, set_x1)
    def get_y1(self): return self.getXY(0, 3, 1, 'y1')  # x1,y1 at points 0 and 3, 1=y
    def set_y1(self, v): return self.setXY(0, 3, 1, v, 'y1') # x1,y1 at points 0 and 3, 1=y
    y1 = shape_property(get_y1, set_y1)
    def get_x2(self): return self.getXY(1, 2, 0, 'x2') # x2,y2 at points 1 and 2, 0=x
    def set_x2(self, v): return self.setXY(1, 2, 0, v, 'x2') # x2,y2 at points 1 and 2, 0=x
    x2 = shape_property(get_x2, set_x2)
    def get_y2(self): return self.getXY(1, 2, 1, 'y2') # x2,y2 at points 1 and 2, 1=y
    def set_y2(self, v): return self.setXY(1, 2, 1, v, 'y2') # x2,y2 at points 1 and 2, 1=y
    y2 = shape_property(get_y2, set_y2)

    def get_arrowStart(self): return self.get('arrowStart')
    def set_arrowStart(self, v): return self.set({'arrowStart': v})
    arrowStart = shape_property(get_arrowStart, set_arrowStart)
    def get_arrowEnd(self): return self.get('arrowEnd')
    def set_arrowEnd(self, v): return self.set({'arrowEnd': v})
    arrowEnd = shape_property(get_arrowEnd, set_arrowEnd)
    def get_lineWidth(self):
        pts = self.pointList
        return utils.distance(pts[0][0], pts[0][1], pts[3][0], pts[3][1])
    def set_lineWidth(self, v):
        self.pointList = utils.getLinePoints(self.x1, self.y1, self.x2, self.y2, v)
        return self.set({'lineWidth': v})
    lineWidth = shape_property(get_lineWidth, set_lineWidth)
    def get_borderWidth(self): return 0
    def set_borderWidth(self, v): pyThrow(t("Cannot set Line's borderWidth"))
    borderWidth = shape_property(get_borderWidth, set_borderWidth)
    def get_border(self): return None
    def set_border(self, v): pyThrow(t("Cannot set Line's border"))
    border = shape_property(get_border, set_border)

    def get_area(self): return self.lineWidth * utils.distance(self.x1, self.y1, self.x2, self.y2)
    area = shape_property(get_area)

    def drawArrows(self, ctx):
        if (not self.arrowEnd and not self.arrowStart): return

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        dist = math.sqrt(dy * dy + dx * dx)
        if dist < 0.01: return
        dx /= dist
        dy /= dist

        normalDx = -dy
        normalDy = dx

        arrowLength = min(50, 10*math.sqrt(self.lineWidth))
        arrowWidth = arrowLength / 3

        def drawArrow(x, y, dir):
            ctx.new_path()
            self.setFillOrStrokeStyle(ctx, self.fill)
            ctx.set_dash([])
            ctx.move_to(x, y)
            ctx.line_to(x + dir * arrowLength * dx - arrowWidth * normalDx,
                y + dir * arrowLength * dy - arrowWidth * normalDy)
            ctx.line_to(x + dir * arrowLength * dx + arrowWidth * normalDx,
                y + dir * arrowLength * dy + arrowWidth * normalDy)
            ctx.close_path()
            ctx.fill_preserve()
            ctx.stroke()

        if self.arrowEnd:
            drawArrow(self.x2, self.y2, -1)
        if self.arrowStart:
            drawArrow(self.x1, self.y1, 1)

    def isPoint(self):
        return self.x1 == self.x2 and self.y1 == self.y2

    def scaleToTarget(self, varName, target):
        if self.isPoint():
            if varName == 'x':
                self.x1 -= target / 2
                self.x2 += target / 2
            elif varName == 'y':
                self.y1 -= target / 2
                self.y2 += target / 2
        self.lineWidth = self.lineWidth

    def get_height(self): return super().get_height()
    def set_height(self, v):
        if self.height == 0:
            self.scaleToTarget('y', v)
        else:
            super().height = 0
    height = shape_property(get_height, set_height)

    def get_width(self): return super().get_width()
    def set_width(self, v):
        if self.width == 0:
            self.scaleToTarget('x', v)
        else:
            super().height = 0
    width = shape_property(get_width, set_width)

    def toString(self):
        args = [self.x1, self.y1, self.x2, self.y2]
        return t('Line{{args}}', {'args': utils.roundedTupleString(args, 2)})

class PolygonInCircle(Polygon):
    def get_radius(self): return self.get('radius')
    def set_radius(self, v):
        self.set({'radius': v})
        self.updatePointList()
        return v
    radius = shape_property(get_radius, set_radius)

    def get_points(self): return self.get('points')
    def set_points(self, v):
        self.set({'points': v})
        self.updatePointList()
        return v
    points = shape_property(get_points, set_points)

    def get_centerX(self): return utils.round2(self.centroid[0])
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = shape_property(get_centerX, set_centerX)
    def get_centerY(self): return utils.round2(self.centroid[1])
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = shape_property(get_centerY, set_centerY)

class RegularPolygon(PolygonInCircle):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getRegularPolygonPoints(attrs['centerX'], attrs['centerY'], attrs['radius'], attrs['points'], 0))
        super().__init__(attrs)

    def updatePointList(self):
        self.pointList = utils.getRegularPolygonPoints(self.centerX, self.centerY, self.radius, self.points, self.rotateAngle)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius, self.points]
        return t('RegularPolygon{{args}}', {'args': utils.roundedTupleString(args, 2)})

class Star(PolygonInCircle):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getStarPoints(attrs['centerX'], attrs['centerY'], attrs['radius'], attrs['points'], None, 0))
        super().__init__(attrs)

    def get_roundness(self):
        result = self.get('roundness')
        if result == 'default':
            return utils.getDefaultRoundness(self.points)
        return result
    def set_roundness(self, v):
        self.set({'roundness': v})
        self.updatePointList()
        return v
    roundness = shape_property(get_roundness, set_roundness)

    def updatePointList(self):
        self.pointList = utils.getStarPoints(self.centerX, self.centerY, self.radius, self.points, self.roundness, self.rotateAngle)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius, self.points]
        return t('Star{{args}}', {'args': utils.roundedTupleString(args, 2)})

class PolygonWithTransform(Polygon):
    def get_transformMatrix(self): return self.get('transformMatrix')
    def set_transformMatrix(self, v): return self.set({'transformMatrix': v})
    transformMatrix = shape_property(get_transformMatrix, set_transformMatrix)

    def multMat(self, trans):
        newTrans = [[0,0], [0,0]]
        for i in range(len(newTrans)):
            for j in range(len(newTrans)):
                for k in range(len(newTrans)):
                    newTrans[i][j] += self.transformMatrix[k][j] * trans[i][k]
        self.transformMatrix = newTrans

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)
        cos = utils.intCos(-degrees)
        sin = utils.intSin(-degrees)
        rotateTrans = [
            [cos, sin],
            [-sin, cos],
        ]
        self.multMat(rotateTrans)

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if k == 1: return
        i = 0 if (varName == 'x') else 1

        trans = [[1, 0], [0, 1]]
        trans[i][i] = k
        self.multMat(trans)

class CMUSound(object):
    processes = []
    def __init__(self, url):
        current_directory = os.path.dirname(__file__)
        sound_path = os.path.join(current_directory, 'sound.py')
        self.soundProcess = subprocess.Popen(
            [sys.executable, sound_path], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=current_directory)
        CMUSound.processes.append(self.soundProcess)
        self.sendProcessMessage({'url': url})

    def sendProcessMessage(self, message):
        packet = bytes(json.dumps(message) + '\n', encoding='utf-8')
        self.soundProcess.stdin.write(packet)
        self.soundProcess.stdin.flush()
        self.soundProcess.stdout.readline()
        self.soundProcess.poll()
        if self.soundProcess.returncode is not None and self.soundProcess.returncode != 0:
            print(self.soundProcess.stderr.read().decode('utf-8'))
            raise Exception('Exception in Sound.')

    def play(self, doLoop, doRestart):
        self.sendProcessMessage({
            'command': 'play',
            'kwargs': {
                'doLoop': doLoop,
                'doRestart': doRestart
            }
        })

    def pause(self):
        self.sendProcessMessage({
            'command': 'pause',
            'kwargs': {}
        })

    def __del__(self):
        self.soundProcess.kill()

def cleanSoundProcesses():
    for p in CMUSound.processes: p.kill()

# clean up processes when the interpreter closes
atexit.register(cleanSoundProcesses)

class CMUImage(PolygonWithTransform):
    def __init__(self, attrs):
        if attrs is not None:
            imageData = loadImage(attrs['url'])

            height, width = imageData['height'], imageData['width']
            right = attrs['left'] + width
            bottom = attrs['top'] + height
            attrs['defaultAlign'] = 'left-top'
            attrs['initialPoints'] = [
                attrs['left'], attrs['top'],
                right, attrs['top'],
                right, bottom,
                attrs['left'], bottom
            ]
            attrs['transformMatrix'] = [
                [1, 0],
                [0, 1],
            ]
            super().__init__(attrs)
            self.attrDefaults = copy.deepcopy(self.attrDefaults)
            self.attrDefaults.update({'fill': None})

    def get_url(self): return self.get('url')
    def set_url(self, v): pyThrow(t("Cannot set Image's url"))
    url = shape_property(get_url, set_url)

    def getScaleAnchor(self): return [self.left, self.top]

    def drawImage(self, ctx):
        mat = self.transformMatrix
        ctx.translate(self.pointList[0][0], self.pointList[0][1])
        ctx.transform(cairo.Matrix(mat[0][0], mat[1][0], mat[0][1], mat[1][1], 0, 0))
        ctx.set_source_surface(activeDrawing.images[hashReference(self.url)], 0, 0)
        ctx.paint_with_alpha(self.opacity / 100)

    def toString(self):
        args = [self.left, self.top, self.width, self.height]
        return t('Image{{args}}', {'args': utils.roundedTupleString(args, 2)})

class Oval(PolygonWithTransform):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getArcPoints(
            attrs['centerX'], attrs['centerY'], attrs['width'], attrs['height'],
            attrs.get('startAngle', None), attrs.get('sweepAngle', None)))
        attrs['transformMatrix'] = [
            [attrs['width'] / 2, 0],
            [0, attrs['height'] / 2],
        ]
        attrs['translation'] = [attrs['centerX'], attrs['centerY']]
        if ('startAngle' not in attrs):
            attrs['startAngle'] = 0
        if ('sweepAngle' not in attrs):
            attrs['sweepAngle'] = 360
        attrs['bezierPoints'] = Oval.getBezierPoints(attrs['startAngle'], attrs['sweepAngle'])
        super().__init__(attrs)

    @staticmethod
    def getBezierPoints(startAngle, sweepAngle):
        offset = utils.toRadians(startAngle)
        remaining = sweepAngle
        bp = []
        while (remaining > 0):
            bp.extend(Oval.getBezierFragment(utils.toRadians(min(90, remaining)), offset))
            offset += math.pi / 2
            remaining -= 90
        return bp

    @staticmethod
    def getBezierFragment(sweepAngle, offsetAngle):
        # Return a cubic Bezier curve that approximates up to 90 degrees of a circle.
        # https://www.tinaja.com/glib/bezcirc2.pdf
        result = [[0, 0], [0, 0], [0, 0], [0, 0]]
        result[3][0] = math.cos(sweepAngle / 2)
        result[3][1] = math.sin(sweepAngle / 2)
        result[0][0] = result[3][0]
        result[0][1] = -result[3][1]

        result[2][0] = (4 - result[3][0]) / 3
        result[2][1] = ((1 - result[3][0]) * (3 - result[3][0])) / (3 * result[3][1])
        result[1][0] = result[2][0]
        result[1][1] = -result[2][1]

        result = utils.rotatePoints(
            result, 
            utils.toDegrees((sweepAngle / 2) + offsetAngle - (math.pi / 2)),
            0, 
            0
        )
        return result

    def get_bezierPoints(self): return self.get('bezierPoints')
    def set_bezierPoints(self, v): return self.set({'bezierPoints': v})
    bezierPoints = shape_property(get_bezierPoints, set_bezierPoints)

    def get_translation(self): return self.get('translation')
    def set_translation(self, v): return self.set({'translation': v})
    translation = shape_property(get_translation, set_translation)

    def makePath(self, ctx):
        ctx.save()
        ctx.new_path()
        ctx.translate(self.translation[0], self.translation[1])
        bp = list(map((lambda p:
            [self.transformMatrix[0][0] * p[0] + self.transformMatrix[0][1] * p[1],
             self.transformMatrix[1][0] * p[0] + self.transformMatrix[1][1] * p[1]]
            ), self.bezierPoints))
        if isinstance(self, Arc):
            ctx.move_to(0, 0)
            ctx.line_to(bp[0][0], bp[0][1])
        else:
            ctx.move_to(bp[0][0], bp[0][1])

        for i in range(0, len(bp) // 4):
            i2 = i * 4
            ctx.curve_to(bp[i2+1][0], bp[i2+1][1], bp[i2+2][0], bp[i2+2][1], bp[i2+3][0], bp[i2+3][1])

        ctx.close_path()
        ctx.restore()

    def addxy(self, varName, d):
        super().addxy(varName, d)
        if d == 0: return
        varIndex = 0 if varName == 'x' else 1
        self.translation[varIndex] += d
        self.translation = self.translation

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if k == 1: return
        i = 0 if varName == 'x' else 1

        cxy = (scaleAnchor or self.getScaleAnchor())[i]
        self.translation[i] = cxy + (self.translation[i] - cxy) * k
        self.translation = self.translation

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)
        self.translation = utils.rotatePoint(self.translation, degrees, cx, cy)

    def toString(self):
        args = [self.centerX, self.centerY, self.width, self.height]
        return t('Oval{{args}}', {'args': utils.roundedTupleString(args, 2)})

class Arc(Oval):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.ovalWidth = attrs['width']
        self.ovalHeight = attrs['height']

    def get_ovalWidth(self): return self.get('ovalWidth')
    def set_ovalWidth(self, v): return self.set({'ovalWidth': v})
    ovalWidth = shape_property(get_ovalWidth, set_ovalWidth)

    def get_ovalHeight(self): return self.get('ovalHeight')
    def set_ovalHeight(self, v): return self.set({'ovalHeight': v})
    ovalHeight = shape_property(get_ovalHeight, set_ovalHeight)

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if (k == 1 or self.ovalWidth is None or self.ovalHeight is None):
            return

        if (self.rotateAngle != 0):
            self.ovalWidth = None
            self.ovalHeight = None
            return

        if (varName == 'x'):
            self.ovalWidth *= k
        elif (varName == 'y'):
            self.ovalHeight *= k

    def get_startAngle(self): return self.get('startAngle')
    def set_startAngle(self, v):
        self.set({'startAngle': v})
        self.regeneratePoints()
        return v
    startAngle = shape_property(get_startAngle, set_startAngle)

    def get_sweepAngle(self): return self.get('sweepAngle')
    def set_sweepAngle(self, v):
        self.set({'sweepAngle': v})
        self.regeneratePoints()
        return v
    sweepAngle = shape_property(get_sweepAngle, set_sweepAngle)

    def regeneratePoints(self):
        self.pointList = utils.getArcPoints(
            0, 0, 2, 2, self.startAngle, self.sweepAngle,
            (self.width + self.height) / 2
        )
        for pt in self.pointList:
            newPt = [
                self.transformMatrix[0][0] * pt[0] + self.transformMatrix[0][1] * pt[1],
                self.transformMatrix[1][0] * pt[0] + self.transformMatrix[1][1] * pt[1]
            ]
            pt[0] = newPt[0] + self.translation[0]
            pt[1] = newPt[1] + self.translation[1]
        self.pointList = self.pointList
        self.bezierPoints = Oval.getBezierPoints(self.startAngle, self.sweepAngle)

    def getRotateAnchor(self):
        return [self.pointList[0][0], self.pointList[0][1]]

    def get_centerX(self): return utils.round2(self.pointList[0][0])
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = shape_property(get_centerX, set_centerX)

    def get_centerY(self): return utils.round2(self.pointList[0][1])
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = shape_property(get_centerY, set_centerY)

class Circle(Oval):
    def __init__(self, attrs):
        attrs['width'] = attrs['height'] = 2 * attrs['radius']
        super().__init__(attrs)
        self._exactRadius = attrs['radius']

    def get_radius(self):
        if self._exactRadius != None:
            return self._exactRadius
        return (self.get('width') + self.get('height')) / 4
    def set_radius(self, v):
        super().set_width(2 * v)
        super().set_height(2 * v)
        self._exactRadius = v
        return v
    radius = shape_property(get_radius, set_radius)

    def get__exactRadius(self): return self.get('_exactRadius')
    def set__exactRadius(self, v): return self.set({'_exactRadius': v})
    _exactRadius = shape_property(get__exactRadius, set__exactRadius)

    def get_width(self): return super().get_width()
    def set_width(self, v): self._exactRadius = None; super().set_width(v); return v
    width = shape_property(get_width, set_width)

    def get_height(self): return super().get_height()
    def set_height(self, v): self._exactRadius = None; super().set_height(v); return v
    height = shape_property(get_height, set_height)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius]
        return t('Circle{{attrs}}', {'attrs': utils.roundedTupleString(args, 2)})

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if (k == 1): return
        self._exactRadius = None

objConstructors = {
  'Arc': Arc,
  'Circle': Circle,
  'Gradient': Gradient,
  'Group': Group,
  'CMUImage': CMUImage,
  'Label': Label,
  'Line': Line,
  'Oval': Oval,
  'Polygon': Polygon,
  'Rect': Rect,
  'RegularPolygon': RegularPolygon,
  'RGB': RGB,
  'Star': Star,
}

BACKGROUND_POINTS = [
  [0, 0],
  [400, 0],
  [0, 400],
  [400, 400],
];
BACKGROUND_DUMMY = object()

class Inspector(object):
    def __init__(self, app):
        self.app = app
        self.keyPoints = None
        self.keyPointsToShapes = None
        self.bestX = self.bestY = self.mouseX = self.mouseY = None

    def getKeyPoints(self, shape):
        x0 = shape.left
        y0 = shape.top
        x1 = shape.right
        y1 = shape.bottom

        points = [
            [x0, y0],
            [x0, y1],
            [x1, y0],
            [x1, y1],
        ]

        if isinstance(shape, Arc):
            points = []
            points.append([shape.pointList[0][0], shape.pointList[0][1]])
            points.append([shape.pointList[1][0], shape.pointList[1][1]])
            numPoints = len(shape.pointList)
            points.append([
                shape.pointList[numPoints-1][0],
                shape.pointList[numPoints-1][1],
            ])
        elif (
            (shape.rotateAngle % 360 != 0 and
                (isinstance(shape, Oval) or isinstance(shape, Rect))) or
            isinstance(shape, Circle) or
            isinstance(shape, Oval) or
            isinstance(shape, Star) or
            isinstance(shape, RegularPolygon) or
            isinstance(shape, Label)
        ):
            points = [[shape.centerX, shape.centerY]]
        elif isinstance(shape, Line):
            points = [
                [shape.x1, shape.y1],
                [shape.x2, shape.y2],
            ]
        elif isinstance(shape, Polygon):
            points = []
            for i in range(len(shape.pointList)):
                points.append([shape.pointList[i][0], shape.pointList[i][1]])

        return list(map(lambda pt: [round(pt[0]), round(pt[1])], points))

    def getKeyPointKey(self, point):
        return '%d-%d' % (point[0], point[1])

    def ensureKeyPointToShapesMap(self):
        if (self.keyPointsToShapes != None):
            return
        self.keyPointsToShapes = dict()
        self.keyPoints = list()

        def addKeyPointTo(shape):
            def addKeyPoint(keyPoint):
                key = self.getKeyPointKey(keyPoint)
                if self.keyPointsToShapes.get(key, None) is None:
                    self.keyPointsToShapes[key] = []
                    self.keyPoints.append(keyPoint)
                self.keyPointsToShapes[key].append(shape)
            return addKeyPoint

        def processShape(shape):
            if shape.isGroup:
                list(map(processShape, shape._shapes))
                return
            if shape.doNotInspect:
                return

            list(map(addKeyPointTo(shape), self.getKeyPoints(shape)))

        processShape(self.app._tlg._shape)
        if self.app.background is not None:
            list(map(addKeyPointTo(BACKGROUND_DUMMY), BACKGROUND_POINTS))


    def getKeyPointExtraShapeInfo(self, kx, ky):
        key = self.getKeyPointKey([kx, ky])
        attrVals = dict()
        def msgsAdd(attr, value):
            if attrVals.get(attr, None) is None:
                attrVals[attr] = set()
            if utils.isNumber(value):
                value = utils.round2(value)
            elif value == True:
                value = t('True')
            elif value == False:
                value = t('False')
            attrVals[attr].add(value)

        if self.keyPointsToShapes.get(key, None) is None:
            return ''

        def gradientToString(color):
            result = ''
            for value in color.colors:
                if isinstance(value, str):
                    result += value
                    result += ', '
                else:
                    result += value.attrs['strVal']
                    result += ', '
            return result[:-2]

        for shape in self.keyPointsToShapes[key]:
            if (shape is BACKGROUND_DUMMY):
                if isinstance(self.app.background, Gradient):
                    msgsAdd(t('background'), gradientToString(self.app.background))
                else:
                    msgsAdd(t('background'), self.app.background)
                continue

            for attr in ['fill', 'border']:
                color = getattr(shape, attr)
                if color is not None:
                    if isinstance(color, Gradient):
                        msgsAdd(t('gradient'), gradientToString(color))
                    else:
                        msgsAdd(t('color'), color)
                elif attr == 'fill' and not isinstance(shape, CMUImage):
                    msgsAdd(t('color'), t('None'))

            def checkAttrDefaults(attrDefaults):
                for attr, defaultVal in attrDefaults:
                    try:
                        val = getattr(shape, attr)
                        if val != None and val != defaultVal:
                            msgsAdd(attr, val)
                    except:
                        pass
            checkAttrDefaults([
                ['opacity', 100],
                ['lineWidth', 2],
                ['radius', None],
                ['dashes', False]
            ])
            if isinstance(shape, Label):
                checkAttrDefaults([
                    ['font', 'Arial'],
                    ['size', 12],
                    ['style', 'normal'],
                    ['bold', False],
                    ['italic', False],
                ])
            if isinstance(shape, Line):
                checkAttrDefaults([
                    ['arrowStart', False],
                    ['arrowEnd', False]
                ])
            if (not isinstance(shape, Label) and not isinstance(shape, Line)):
                checkAttrDefaults([['borderWidth', 2]])
            if isinstance(shape, Star):
                checkAttrDefaults([
                    ['roundness', utils.getDefaultRoundness(shape.points)],
                ])
            if isinstance(shape, Star) or isinstance(shape, RegularPolygon):
                checkAttrDefaults([['points', None]])
            if shape.rotateAngle % 360 != 0:
                msgsAdd('rotateAngle', shape.rotateAngle)
            if isinstance(shape, Arc):
                checkAttrDefaults([
                    ['sweepAngle', None],
                    ['startAngle', None],
                ])
                if (shape.ovalWidth != None and shape.ovalHeight != None):
                    msgsAdd(
                        t('oval size'),
                        '(%d, %d)' % (
                            utils.round2(shape.ovalWidth),
                            utils.round2(shape.ovalHeight)
                        )
                    )
            if (
                (isinstance(shape, Oval) and
                    not isinstance(shape, Circle) and
                    not isinstance(shape, Arc)) or
                (shape.rotateAngle % 360 != 0 and isinstance(shape, Rect))
            ):
                pts = shape.getApproxPoints()
                unrotatedPoints = utils.rotatePoints(
                    pts,
                    -shape.rotateAngle,
                    shape.centerX,
                    shape.centerY
                )
                bounds = utils.getBoxDims(unrotatedPoints)
                msgsAdd(
                    t('size'),
                    '(%d, %d)' % (
                        utils.round2(bounds['width']),
                        utils.round2(bounds['height'])
                    )
                )
        msgs = [self.getPointStr(kx, ky)];
        for attr in attrVals:
            for val in attrVals[attr]:
                msgs.append('%s: %s' % (attr, str(val)))
        return '\n'.join(msgs)

    def getPointStr(self, x, y):
        return '(%d, %d)' % (x, y)

    def nearestKeyPoint(self, x, y):
        bestD = 100000000
        bestX = None
        bestY = None
        for pt in self.keyPoints:
            d = (pt[0] - x) ** 2 + (pt[1] - y) ** 2
            if d < bestD:
                bestD = d
                [bestX, bestY] = pt
        return [bestX, bestY]

    def reset(self):
        self.mouseX = self.mouseY = None
        self.clearCache()

    def clearCache(self):
        self.keyPoints = self.keyPointsToShapes = None
        self.bestX = self.bestY = None

    def setMousePosition(self, x, y):
        self.mouseX = x
        self.mouseY = y
        self.bestX = self.bestY = None

    def computeBestPoint(self):
        if self.mouseX is None or self.mouseX is None:
            return
        self.ensureKeyPointToShapesMap()
        bestX, bestY = self.nearestKeyPoint(self.mouseX, self.mouseY)

        if (
            bestX is None or
            utils.distance(self.mouseX, self.mouseY, bestX, bestY) > 300
        ):
            self.bestX = self.bestY = None
        else:
            self.bestX = bestX
            self.bestY = bestY

    def draw(self, ctx):
        self.computeBestPoint()
        if self.bestX is None or self.bestY is None:
            return

        black = (0, 0, 0)
        red = (0, 0, 255)
        gold = (0, 215, 255)
        white = (255, 255, 255)

        for pt in self.keyPoints:
            ctx.new_path()
            ctx.arc(pt[0], pt[1], 2, 0, 2 * math.pi)
            ctx.close_path()
            ctx.set_source_rgba(*black)
            ctx.set_line_width(2)
            ctx.stroke_preserve()
            ctx.set_source_rgba(*gold)
            ctx.fill()

        ctx.set_source_rgba(*red)
        for r in [5, 4, 3, 2, 1]:
            ctx.set_source_rgb(*(red if r % 2 == 1 else black))
            ctx.new_path()
            ctx.arc(self.bestX, self.bestY, r, 0, 2 * math.pi)
            ctx.close_path()
            ctx.fill()

        def textWidth(text):
            return ctx.text_extents(text)[2]

        def drawCenteredText(text, x, y):
            x, y = int(x), int(y)
            _, _, width, _, _, _ = ctx.text_extents(text)
            ctx.move_to(x - width / 2, y)
            ctx.show_text(text)

        ctx.select_font_face(*getFont('arial'))
        ctx.set_font_size(12)
        pointLabelText = self.getPointStr(self.bestX, self.bestY)
        w = textWidth(pointLabelText)
        h = 12
        margin = 10
        pointLabelCenterX = min(
            400 - margin - w / 2,
            max(margin + w / 2, self.bestX - 10)
        )
        pointLabelCenterY = min(
            400 - margin - h / 2,
            max(margin + h / 2, self.bestY - 10)
        )

        ctx.set_source_rgba(*white, 0.5)
        ctx.rectangle(
            pointLabelCenterX - w / 2 - 2,
            pointLabelCenterY - h / 2 - 2,
            w + 4,
            h + 4
        )
        ctx.fill()

        ctx.set_source_rgba(*black)
        drawCenteredText(
            pointLabelText,
            pointLabelCenterX,
            pointLabelCenterY + h / 2 - 2,
        )

        minTop = 10
        if pointLabelCenterX > 300 and pointLabelCenterY < 50:
            minTop = pointLabelCenterY + margin
        info = self.getKeyPointExtraShapeInfo(self.bestX, self.bestY)
        infoLines = info.split('\n')
        ctx.set_source_rgba(*white, 0.5)
        infoWidth = 0
        newLines = []
        maxWidth = 300

        def shortenLine(line):
            splitLine = line.split(',')
            return [splitLine.pop(), ''.join(splitLine)]

        for line in infoLines:
            if textWidth(line) < maxWidth:
                newLines.append(line)
            else:
                leftover = ''
                while textWidth(line) > maxWidth:
                    lastWord, line = shortenLine(line)
                    if len(leftover) > 0:
                        leftover = ',' + leftover
                    leftover = lastWord + leftover
                if len(leftover) > 0:
                    line = line + ','
                newLines.append(line, leftover)

        for line in newLines:
            infoWidth = max(infoWidth, textWidth(line))

        lineHeight = 12
        infoHeight = lineHeight * len(newLines)
        ctx.rectangle(
            400 - 2 * margin - infoWidth,
            minTop,
            infoWidth + 2 * margin,
            infoHeight + margin
        )
        ctx.fill()
        ctx.set_source_rgba(*black)
        verticalOffset = 0
        for line in newLines:
            firstword = line[0:line.find(':')+1]
            newline = line[line.find(':')+1:]
            ctx.select_font_face(*getFont('arial', isBold=True))
            firstwordWidth = textWidth(firstword)
            ctx.select_font_face(*getFont('arial'))
            newlineWidth = textWidth(newline)
            ctx.select_font_face(*getFont('arial', isBold=True))

            drawCenteredText(
                firstword,
                400 -
                    margin -
                    infoWidth / 2 -
                    (newlineWidth + firstwordWidth) / 2 +
                    firstwordWidth / 2,
                minTop + lineHeight + verticalOffset
            )

            ctx.select_font_face(*getFont('arial'))
            drawCenteredText(
                newline,
                400 -
                    margin -
                    infoWidth / 2 +
                    (newlineWidth + firstwordWidth) / 2 -
                    newlineWidth / 2,
                minTop + lineHeight + verticalOffset
            )
            verticalOffset += lineHeight

class ShapeLogicInterface(object):
    def toEnglish(self, *args, **kwargs):
        return toEnglish(*args, **kwargs)

    def accentCombinations(self, *args, **kwargs):
        return accentCombinations(*args, **kwargs)

    def t(self, *args, **kwargs):
        return t(*args, **kwargs)

    def setLanguage(self, language):
        global cmuGraphicsLanguage
        if language in supportedLanguages:
            cmuGraphicsLanguage = language

    def rgb(self, r, g, b):
        return RGB(r, g, b)

    def gradient(self, *colors, start=None, **kwargs):
        for keyword in kwargs:
            if toEnglish(keyword, 'shape-attr') == 'start':
                start = kwargs[keyword]
            else:
                raise Exception("TypeError: %s() got an unexpected keyword argument '%s'" % (t('gradient'), keyword))

        return Gradient(list(colors), 'center' if start is None else start)

    def newSound(self, url):
        checkArgCount(None, t('Sound'), [t('url')], (url,))
        checkString(t('Sound'), t('url'), url, False)
        return CMUSound(url)

    def slNew(self, className, args):
        return (objConstructors[className])(args)

    def slApply(self, slObj, method, args, kwargs):
        args = list(args)
        # 1. replace student shapes with sl shapes
        for i in range(len(args)):
            if hasattr(args[i], '_shape'):
                args[i] = args[i]._shape
        # 2. make the call
        result = (getattr(slObj, method))(*args, **kwargs)
        # 3. replace sl shapes with student shapes and return
        if isinstance(result, Shape):
            if hasattr(result, 'studentShape'):
                utils.internalError('Need to wrap new sl shape in student shape')
            result = result.studentShape
        return result

    def slGet(self, slObj, attr):
        if not hasattr(slObj, attr):
            pyThrow(t('No such attribute: {{attr}}', {'attr': attr}))
        result = getattr(slObj, attr)
        if callable(result):
            result = lambda *args, **kwargs: self.slApply(slObj, attr, args, kwargs)
        elif hasattr(result, 'studentShape'):
            result = result.studentShape
        return result

    def slSetWithTypeCheck(self, obj, attr, val):
        className = obj.__class__.__name__
        if shapeAttrs.get(attr, None) is not None:
            shapeAttrs[attr].typeCheckFn(obj, attr, val, False)
            setattr(obj, attr, val)
        elif hasattr(obj, attr) and callable(getattr(obj, attr)):
            pyThrow(
              t("{{methodName}} is a function. You can't assign to it.", {
                'methodName': f'{className}.{attr}',
              })
            );
        else:
            utils.internalError(
                f'No type check function found for {className}.{attr}')
        return val

    def slSetAppProperty(app, propName, value):
        if propName == 'maxShapeCount':
            checkNonNegative(t('app'), propName, value, False)
        elif propName == 'beatsPerMinute':
            checkNumber(t('app'), propName, value, False)
        elif propName == 'background':
            checkColor(t('app'), propName, value, False)
        activeDrawing.appProperties[propName] = value

    def slGetAppProperty(app, propName):
        return activeDrawing.appProperties[propName]

    def slInitShape(self, clsName, argNames, args, kwargs):
        if clsName == 'Image':
            clsName = 'CMUImage'
        checkArgCount(clsName, None, argNames, args)
        for attr in kwargs:
            if shapeAttrs.get(attr, None) is None:
                pyThrow(t('"{{attr}}" is not a valid shape constructor argument', {'attr': attr}))
        if kwargs.get('align', None) is not None and clsName == 'Polygon':
            pyThrow(t('"{{align}}" is not a valid Polygon constructor argument', {'align': t('align')}))
        constructorArgs = dict()
        for i in range(0, len(argNames)):
            attr = argNames[i]
            shapeAttrs[attr].typeCheckFn(clsName, attr, args[i], False)
            constructorArgs[argNames[i]] = args[i]
        shape = self.slNew(clsName, constructorArgs)
        try:
            align = None
            if 'align' in kwargs:
                align = kwargs['align']
                del kwargs['align']
            for attr in kwargs:
                self.slSetWithTypeCheck(shape, attr, kwargs[attr])
            if align is not None:
                checkAlign(shape, t('align'), align, False)
                xPoint = constructorArgs.get('left', None) if constructorArgs.get('centerX', None) is None else constructorArgs['centerX']
                yPoint = constructorArgs.get('top', None) if constructorArgs.get('centerY', None) is None else constructorArgs['centerY']
                shape.doAlign(xPoint, yPoint, align)
        except Exception as e:
            activeDrawing.tlg.remove(shape)
            raise e
        return shape

    def setTopLevelGroup(self, tlg):
        activeDrawing.tlg = tlg
