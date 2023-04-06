from typing import List
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
	_hardware: List[Hardware] = []
	_software: List[Software] = []
	
	@staticmethod
	def __find_entity_from_name(entity_name, entities):
		for entity in entities:
			if entity_name == entity.name:
				return entity
	
	@staticmethod
	def __try_to_install_software(hardware_name, software: Software):
		hardware = System.__find_entity_from_name(hardware_name, System._hardware)
		if not hardware:
			return "Hardware does not exist"
		
		hardware.install(software)
		System._software.append(software)
		
	@staticmethod
	def register_power_hardware(name: str, capacity: int, memory: int):
		hardware = PowerHardware(name, capacity, memory)
		System._hardware.append(hardware)
	
	@staticmethod
	def register_heavy_hardware(name: str, capacity: int, memory: int):
		hardware = HeavyHardware(name, capacity, memory)
		System._hardware.append(hardware)
	
	@staticmethod
	def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
		software = ExpressSoftware(name, capacity_consumption, memory_consumption)
		return System.__try_to_install_software(hardware_name, software)
	
	@staticmethod
	def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
		software = LightSoftware(name, capacity_consumption, memory_consumption)
		return System.__try_to_install_software(hardware_name, software)
		
	@staticmethod
	def release_software_component(hardware_name: str, software_name: str):
		hardware = System.__find_entity_from_name(hardware_name, System._hardware)
		software = System.__find_entity_from_name(software_name, System._software)
		
		if not hardware or not software:
			return "Some of the components do not exist"
		
		hardware.uninstall(software)
		System._software.remove(software)
	
	@staticmethod
	def analyze():
		result = [
			"System Analysis",
			f"Hardware Components: {len(System._hardware)}",
			f"Software Components: {len(System._software)}",
			f"Total Operational Memory: "
			f"{sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}",
			f"Total Capacity Taken: "
			f"{sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}",
		]
		
		return '\n'.join(result)
	
	@staticmethod
	def system_split():
		result = []
		for hardware in System._hardware:
			result.append(
				f"Hardware Component - {hardware.name}\n"
				f"Express Software Components: {hardware.express_components}\n"
				f"Light Software Components: {hardware.light_components}\n"
				f"Memory Usage: {hardware.memory_occupied} / {hardware.memory}\n"
				f"Capacity Usage: {hardware.capacity_occupied} / {hardware.capacity}\n"
				f"Type: {hardware.hardware_type}\n"
				f"Software Components: {hardware.all_components}"
			)
		
		return '\n'.join(result)