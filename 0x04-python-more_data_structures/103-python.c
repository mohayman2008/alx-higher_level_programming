#include <stdio.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj;
	int i = 0, max;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		fprintf(stdout, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_obj = (PyBytesObject *) p;

	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	max = PyBytes_Size(p) + 1 > 10 ? 10 : PyBytes_Size(p) + 1;
	printf("  first %d bytes:", max);
	for (; i < max ; i++)
		printf(" %02x", (unsigned char)((bytes_obj->ob_sval)[i]));
	putchar('\n');
}

void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	PyObject *element;

	if (PyList_Check(p))
	{
		list_obj = (PyListObject *) p;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", list_obj->allocated);

		for (int i = 0 ; i < PyList_Size(p) ; i++)
		{
			element = list_obj->ob_item[i];
			printf("Element %d: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
		}
	}
}
