def input_parameters() -> list[str]:
	"""
	Принимает строку от пользователя с входными параметрами.
	"""
	print('Доступные фигуры: square, circle.')
	return input("Введите параметры через пробел: фигура размер цвет имя файла: ").split()


def creator_svg(figure: str = 'square', size: str = '100', color: str = '#FFFFFF') -> str:
	"""
	Принимает на вход название фигуры, размер, цвет.
	Формирует и отдает SVG-строку, если запрошенная фигура имеется в словаре.
	"""
	figures = {'square': f'  <rect fill="{color}" width="{size}" height="{size}"/>',
			   'circle': f'  <circle fill="{color}" cx="{size}" cy="{size}" r="{size}" />'
			   }


	svg = f"""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
{figures.get(figure)}
</svg>
"""
	return svg


def write_file_svg(svg: str, path_file: str = './new_figure.svg') -> None:
	with open(path_file, 'w', encoding='UTF-8') as file:
		file.write(svg)
		print('Файл записан.')

figure, size, color, path_file = input_parameters()
svg = creator_svg(figure, size, color)
write_file_svg(svg, path_file)
