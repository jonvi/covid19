import parser
import plotter


def run():
    df = parser.loadData()
    df = parser.divideData(df)
    df = parser.sanitizeData(df)
    plotter.plot(df)

if __name__ == "__main__":
    run()
