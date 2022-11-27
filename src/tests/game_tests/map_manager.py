import unittest
from game.managers.map import Map


class MapManagerTest(unittest.TestCase):
    def test_map_calculating_road_angle(self):
        test_map = Map({'map': [{'x': 0, 'y': 0}, ],
                        'base': {'x': 100, 'y': 100}})
        test_map2 = Map({'map': [{'x': 0, 'y': 100}, ],
                         'base': {'x': 100, 'y': 0}})

        test_map3 = Map({'map': [{'x': 100, 'y': 0}, ],
                         'base': {'x': 0, 'y': 100}})
        test_map4 = Map({'map': [{'x': 100, 'y': 100}, ],
                         'base': {'x': 0, 'y': 0}})

        test_map5 = Map({'map': [{'x': 100, 'y': 0}, ],
                         'base': {'x': 100, 'y': 100}})
        test_map6 = Map({'map': [{'x': 100, 'y': 100}, ],
                         'base': {'x': 100, 'y': 0}})

        test_map7 = Map({'map': [{'x': 0, 'y': 100}, ],
                         'base': {'x': 100, 'y': 100}})
        test_map8 = Map({'map': [{'x': 100, 'y': 100}, ],
                         'base': {'x': 0, 'y': 100}})

        self.assertEqual(test_map.get_road_angle(0), 45.0)
        self.assertEqual(test_map2.get_road_angle(0), 315.0)
        self.assertEqual(test_map3.get_road_angle(0), 135.0)
        self.assertEqual(test_map4.get_road_angle(0), 225.0)

        self.assertEqual(test_map5.get_road_angle(0), 90)
        self.assertEqual(test_map6.get_road_angle(0), 270)
        self.assertEqual(test_map7.get_road_angle(0), 0)
        self.assertEqual(test_map8.get_road_angle(0), 180)


if __name__ == '__main__':
    unittest.main()
