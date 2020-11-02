#Program to do CRUD operations for any domain

menu_file = "Menu.cfg"
fields_file = "fields_file.cfg"
data_file = "Data.dat"
updatable_fields = "updatable_fileds.cfg"
file_not_found_message = "File not found or error in opening the file"

with open(menu_file) as f_menu:
	menu = f_menu.read()
f_menu.close()

with open(fields_file) as f_fields:
	field_names = f_fields.readlines()
f_fields.close()

with open(data_file, 'r') as f_data:
	record = f_data.read();
f_data.close()
records = eval(record)



def create_record():
	field_values = []
	record_status = 'A'
	field_values.append(record_status)
	for field_name in field_names:
		print(field_name.rstrip() + ": ", end = "")
		field_value = input()
		field_values.append(field_value)
	records.append(field_values)
	with open(data_file, 'w') as f_data:
			f_data.write(str(records))
	f_data.close()
	print("--------------")
	print("Record saved successfully.")


def read_records():
	count_of_records = 0
	for field_value in records:
		if field_value[0] == 'A':
			print_record(field_value)
			print("----------------------")
			count_of_records += 1
	print('Count of records:', count_of_records)


def update_record():
	print("Enter " + field_names[0].rstrip() + ":", end = "")
	user_input_id = input()
	is_updated = 0
	updaterecord_status = 0
	with open(updatable_fields, 'r') as f_updatables:
		list_of_updatable_fields = f_updatables.readlines()
	f_updatables.close()
	for field_value in records:
		if field_value[0] == 'A' and field_value[1] == str(user_input_id):
			update_record_status = 1
			counter = 1
			for updatable_field in list_of_updatable_fields:
				print(str(counter) + "." + "update" + field_names[eval(updatable_field) - 1].rstrip())
				counter = counter + 1
			try:
				user_option = int(input("Enter option: "))
			except Exception:
				print("Invalid option")
			print("Enter new " + field_names[eval(list_of_updatable_fields[user_option - 1]) - 1].rstrip() + ": ", end = "")
			field_value[eval(list_of_updatable_fields[user_option - 1])] = input()
			print(field_names[eval(list_of_updatable_fields[user_option - 1]) - 1].rstrip() + " updated successfully.")
			break
	if update_record_status == 0:
		print("Record not found")
	else:
		with open(data_file, 'w') as f_data:
			f_data.write(str(records))
		f_data.close()

def delete_record():
	print("Enter " + field_names[0].rstrip() + ":", end = "")
	user_input_id = input()
	is_deactivated = 0
	for field_values in records:
		is_deactivated = 1
		if(field_values[0] == 'A' and field_values[1] == user_input_id):
			is_deactivated == 1
			field_values[0] = 'D'
			break
	if is_deactivated == 0:
		print('Record not found.')
	else:
		with open(data_file, 'w') as f_data:
			f_data.write(str(records))
		f_data.close()
		print("Record deactivated successfully.")

def search_record():
	print("Enter " + field_names[0].rstrip() + ":", end = "")
	user_input_id = input()
	search_record_status = 0
	for field_value in records:
		if field_value[0] == 'A' and field_value[1] == str(user_input_id):
			search_record_status = 1
			print_record(field_value)
			break
	if search_record_status == 0:
		print('Record not found.')

def print_record(field_value):
	index = 1
	for field_name in field_names:
		print(field_name.rstrip() + ": ", end = "")
		print(field_value[index])
		index = index + 1


functionsList = [create_record, read_records, update_record, delete_record, search_record, exit]

while True:
	print(menu)
	user_input = input("Enter you input: ")
	user_input = int(user_input)
	functionsList[user_input - 1]()
