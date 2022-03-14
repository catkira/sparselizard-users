#include "sparselizard_wrapper.h"

namespace py = pybind11;

void init_densemat(py::module &m)
{
    py::class_<densemat>(m, "densemat")
    
        .def(py::init<>())
        .def(py::init<int, int>(), py::arg("numberofrows"), py::arg("numberofcolumns"))
        .def(py::init<int, int, double>(), py::arg("numberofrows"), py::arg("numberofcolumns"), py::arg("initvalue"))
        .def(py::init<int, int, std::vector<double>>(), py::arg("numberofrows"), py::arg("numberofcolumns"), py::arg("valvec"))
        .def(py::init<int, int, double, double>(), py::arg("numberofrows"), py::arg("numberofcolumns"), py::arg("init"), py::arg("step"))
        .def(py::init<std::vector<densemat>>(), py::arg("input"))

        .def("countrows", &densemat::countrows)
        .def("countcolumns", &densemat::countcolumns)

        .def("count", &densemat::count)

        .def("print", &densemat::print)
        .def("printsize", &densemat::printsize)

        .def("getvalues", [](densemat &self, py::list& values){
                std::cout<<"running getvalues wrapper"<<std::endl;
                const unsigned int numValues = self.count();
                std::vector<double> valuesWrapped(numValues);
                self.getvalues(valuesWrapped);
                for(size_t index = 0; index < numValues; index++){
                    values.append(valuesWrapped[index]);
                }
            }, py::arg("values"))
            
        .def("getvalues", [](densemat &self){
                std::cout<<"running getvalues wrapper"<<std::endl;
                double *valptr = self.getvalues();
                py::list values;               
                const unsigned int numValues = self.count();
                for(size_t index = 0; index < numValues; index++){
                    values.append(valptr[index]);
                }
                return values;
            })               
    ;
}

