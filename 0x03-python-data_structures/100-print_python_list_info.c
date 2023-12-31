/**
 * print_python_list_info -This will prints basic info about python lists.
 * @p: A pyobject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List =  %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		print("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		print("%s\n", Py_TYPE(obj)->tp_name);
	}
}
