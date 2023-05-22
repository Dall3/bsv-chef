import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.controllers.receipecontroller import ReceipeController
# add your test case implementation here


@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_1(mockReadiness):
    """
    Less than 0.1 shall return None
    """
    mockReadiness.return_value = 0
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    wholegrain = {
    "name": "Whole Grain Bread",
    "diets": [
        "normal", "vegetarian", "vegan"
    ],
    "ingredients": {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }}
    available = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(wholegrain, available, diet)
    assert result == None

@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_2(mockReadiness):
    """
    Between 0.1 and < 1 shall return the mockReadiness value
    """
    mockReadiness.return_value = 0.1
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    wholegrain = {
    "name": "Whole Grain Bread",
    "diets": [
        "normal", "vegetarian", "vegan"
    ],
    "ingredients": {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }}
    available = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(wholegrain, available, diet)
    assert result == 0.1

@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_3(mockReadiness):
    """
    1 shall return the mockReadiness value
    """
    mockReadiness.return_value = 1
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    wholegrain = {
    "name": "Whole Grain Bread",
    "diets": [
        "normal", "vegetarian", "vegan"
    ],
    "ingredients": {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }}
    available = {
        "Flour": 500,
        "Walnuts": 20,
        "Yeast": 1,
        "Salt": 10,
        "Vinegar": 30
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(wholegrain, available, diet)
    assert result == 1

@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_4(mockReadiness):
    """
    Not compatible with diet with readiness value < 0.1
    """
    mockReadiness.return_value = 0
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    pancakes = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }}
    available = {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(pancakes, available, diet)
    assert result == None

@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_5(mockReadiness):
    """
    Not compatible with diet with readiness value 0.1 < 1
    """
    mockReadiness.return_value = 0.1
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    pancakes = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }}
    available = {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(pancakes, available, diet)
    assert result == None

@pytest.mark.unit
@patch('src.controllers.recipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_6(mockReadiness):
    """
    Not compatible with diet with readiness value 1
    """
    mockReadiness.return_value = 1
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    pancakes = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }}
    available = {
        "Egg": 3,
        "Milk": 100,
        "Yoghurt": 200,
        "Flour": 150,
        "Baking Powder": 1,
        "Salt": 5,
        "Sugar": 25
    }
    diet = "vegan"
    result = sut.get_readiness_of_receipes(pancakes, available, diet)
    assert result == None
