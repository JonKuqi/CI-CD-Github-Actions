from core.PearsonCorrelation import PearsonCorrelation



def test_placeholder():
    assert True


def test_predict_for_user():
    #result = PearsonCorrelation.predict_for_user(1)

    #print(result)

    assert True

def test_pearson_correlation():
    result = PearsonCorrelation.pearson_correlation([1, 2, 5, 10],[20, 30, 1, 2, 5], 0.5, 0.5)

    result = "{:.4f}".format(result)

    assert result == '0.1874'

