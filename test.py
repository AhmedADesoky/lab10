import unittest
from app import app , get_tasks , add_task

class Test(unittest.TestCase):
    def test_add_task(self):
        add_task("Task 1")
        self.assertIn("Task 1" , get_tasks())

    def test_get_task(self):
        add_task("Task 1")
        add_task("Task 2")
        tasks = get_tasks()
        self.assertEqual(tasks, ["Task 1" , "Task 1", "Task 2"])




if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)