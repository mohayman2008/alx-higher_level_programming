#include <stdio.h>
#include <sys/types.h>
#include <pyport.h>
#include <assert.h>
#include <object.h>
#include <unicodeobject.h>
#include <tupleobject.h>
#include <structseq.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <pystrtod.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj;
	int i = 0, max;

	setbuf(stdout, NULL);
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

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		float_obj = (PyFloatObject *) p;
		printf("  value: %s\n", PyOS_double_to_string(float_obj->ob_fval,
							'r', 0, Py_DTSF_ADD_DOT_0, NULL));
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	PyObject *element;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		list_obj = (PyListObject *) p;
		printf("[*] Size of the Python List = %ld\n", list_obj->ob_base.ob_size);
		printf("[*] Allocated = %lu\n", list_obj->allocated);

		for (int i = 0 ; i < list_obj->ob_base.ob_size ; i++)
		{
			element = list_obj->ob_item[i];
			printf("Element %d: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			if (PyFloat_Check(element))
				print_python_float(element);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
