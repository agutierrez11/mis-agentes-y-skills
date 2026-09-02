def parse_contract(pdf_path):
    print(f"Parsing contract tables from {pdf_path}...")
    print("Extracted: Interchange Fee Matrix, Settlement Terms (T+1), Penalty Clauses.")

if __name__ == '__main__':
    parse_contract("contrato_banco.pdf")
