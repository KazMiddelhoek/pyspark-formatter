from pyspark_formatter import main


def test_main(tmp_path) -> None:
    tmp_file = tmp_path / "tmp.py"
    tmp_file.write_text("""w = Window().orderBy(["a"]).partitionBy(["b"])
df1.join(df2, ["c"]).select(f.col("c"))""")

    main.run([str(tmp_file)])

    with open(tmp_file) as f:
        result = f.read()
    assert (
        result
        == """w = Window().orderBy("a").partitionBy("b")
df1.join(df2, "c").select("c")"""
    )
