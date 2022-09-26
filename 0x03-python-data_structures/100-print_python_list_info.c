#include <stdio.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);

		for (int i = 0 ; i < PyList_Size(p) ; i++)
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
