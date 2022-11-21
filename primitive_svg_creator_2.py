class LineSVG:
	"""
	Класс Линия SVG.
	"""
	def __init__(self):
		self.coordinates = input('Введите координаты x1 x2 y1 y2: ').strip()
		self.width = input('Введите ширину линии: ').strip()
		self.color = input('Введите цвет: ').strip()

	def get_svg(self) -> str:
		x1, x2, y1, y2 = self.coordinates.split(' ')
		svg = f"""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <line x1="{x1}" x2="{x2}" y1="{y1}" y2="{y2}" stroke="{self.color}" stroke-width="{self.width}" />
</svg>
"""
		return svg


class SquareSVG:
	"""
	Класс Квадрат SVG.
	"""
	def __init__(self) -> None:
		self.size = input('Введите размер: ').strip()
		self.color = input('Введите цвет: ').strip()

	def get_svg(self) -> str:
		svg = f"""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <rect fill="{self.color}" width="{self.size}" height="{self.size}"/>
</svg>
"""
		return svg


class CircleSVG:
	"""
	Класс Круг SVG.
	"""
	def __init__(self) -> None:
		self.size = input('Введите размер: ').strip()
		self.color = input('Введите цвет(название или HEX): ').strip()

	def get_svg(self) -> str:
		svg = f"""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <circle fill="{self.color}" cx="{self.size}" cy="{self.size}" r="{self.size}" />
</svg>
"""
		return svg


def input_figure() -> str:
	"""
	Принимает строку от пользователя с желаемой фигурой. Проверяет есть ли такая в словаре.
	Выводит сообщение ошибки и запрашивает снова, если фигуры нет в словаре.
	Формирует SVG строку.

	:return: SVG-строка  фигуры.
	"""

	figures = {'square': SquareSVG, 'circle': CircleSVG, 'line': LineSVG}
	figures_str = tuple(figures.keys())

	while True:
		try:
			figure: str = input(f'Введите фигуру {figures_str}: ').strip()
			if figure not in figures:
				raise KeyError
			figure_svg = figures.get(figure)()
			return figure_svg.get_svg()
		except KeyError:
			print(f'Такую фигуру не возможно создать. Выберете из списка: {figures_str}')
			continue


def write_file_svg(svg: str):
	"""
	Запрашивает имя(путь) файла.
	Сохраняет полученный SVG-строку в файл.
	"""
	path_file = input('Введите имя для сохранения файла(name.svg): ')
	with open(path_file, 'w', encoding='UTF-8') as file:
		file.write(svg)
		print('Файл записан.')


write_file_svg(input_figure())
