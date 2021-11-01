#include "sparselizard_wrapper.h"

namespace py = pybind11;

void init_vec(py::module &m)
{
    py::class_<vec>(m, "vec")
    
        .def(py::init<>())
        .def(py::init<formulation>(), py::arg("formul"))

        .def("size", &vec::size)

        .def("updateconstraints", &vec::updateconstraints)

        .def("setvalue", static_cast<void (vec::*)(int, double, std::string)>(&vec::setvalue), py::arg("address"), py::arg("value"), py::arg("op")="set")
        .def("getvalue", static_cast<double (vec::*)(int)>(&vec::getvalue), py::arg("address"))

        .def("setvalue", static_cast<void (vec::*)(port, double, std::string)>(&vec::setvalue), py::arg("prt"), py::arg("value"), py::arg("op")="set")
        .def("getvalue", static_cast<double (vec::*)(port)>(&vec::getvalue), py::arg("prt"))

        .def("setdata", static_cast<void (vec::*)(int, field, std::string)>(&vec::setdata), py::arg("physreg"), py::arg("myfield"), py::arg("op")="set")
        .def("setdata", static_cast<void (vec::*)()>(&vec::setdata))

        .def("automaticupdate", &vec::automaticupdate, py::arg("updateit"))
        .def("noautomaticupdate", &vec::noautomaticupdate)

        .def("write", &vec::write, py::arg("filename"))
        .def("load", &vec::load, py::arg("filename"))
        .def("print", &vec::print)

        .def("norm", &vec::norm, py::arg("type")="2")
        .def("sum", &vec::sum)
        
        
        .def("__pos__", static_cast<vec (vec::*)()>(&vec::operator+))
        .def("__neg__", static_cast<vec (vec::*)()>(&vec::operator-))
        
        // operator (vec, double)
        .def("__mul__", [](vec &a, double &b) { return a*b;}, py::is_operator())
        .def("__truediv__", [](vec &a, double &b) { return a/b;}, py::is_operator())
        
        // operator (vec, vec)
        .def("__add__", [](vec &a, vec &b) { return a+b;}, py::is_operator())
        .def("__sub__", [](vec &a, vec &b) { return a-b;}, py::is_operator())
        
        // operator (double, vec)
        .def("__rmul__", [](vec &a, double &b) { return b*a;}, py::is_operator())
        
    ;
}

