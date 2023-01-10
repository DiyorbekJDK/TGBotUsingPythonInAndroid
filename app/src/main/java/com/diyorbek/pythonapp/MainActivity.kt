package com.diyorbek.pythonapp

//noinspection SuspiciousImport
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.chaquo.python.Kwarg
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

//import java.beans.JavaBean


class MainActivity : AppCompatActivity() {
    val TAG = "PythonOnAndroid"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        initPython()
        //callPythonCode()
    }

    // Инициализируем среду Python
    fun initPython() {
        if (!Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }
    }

    // вызываем код Python
    //fun callPythonCode() {
    //val py = Python.getInstance()
    // Вызов функции приветствия в модуле hello.py и передача параметра
    // Эквивалентное использование: py.getModule ("hello"). Get ("greet"). Call ("Android");
    // py.getModule("hello").callAttr("greet", "Android")

    // Вызов встроенной функции python help () и вывод справочной информации
//        py.builtins["help"]!!.call()
//        val obj1 = py.getModule("hello").callAttr("add", 2, 3)
    // Измените возвращаемое значение Python на тип Integer в Java
//        val sum = obj1.toJava(Int::class.java)
//        Log.d(TAG, "add = $sum")

    // Вызов функции python, передача именованного параметра, эквивалент sub (10, b = 1, c = 3)
//        val obj2 = py.getModule("hello").callAttr("sub", 10, Kwarg("b", 1), Kwarg("c", 3))
//        val result = obj2.toJava(Int::class.java)
//        Log.d(TAG, "sub = $result")

    // Вызов функции Python для преобразования возвращенного списка в Python в список Java
//        val obj3 = py.getModule("hello").callAttr("get_list", 10, "xx", 5.6, 'c')
//        val pyList = obj3.asList()
//        Log.d(TAG, "get_list = $pyList")

    // Передаем объект Java ArrayList в Python для использования
//        val params: MutableList<PyObject> = ArrayList()
//        params.add(PyObject.fromJava("alex"))
//        params.add(PyObject.fromJava("bruce"))
//        py.getModule("hello").callAttr("print_list", params)

    // Вызов классов Java в Python
//        val obj4 = py.getModule("hello").callAttr("get_java_bean")
//        val data: java.beans.JavaBean =
//            obj4.toJava<java.beans.JavaBean>(java.beans.JavaBean::class.java)
//        data.print()
    //}
}