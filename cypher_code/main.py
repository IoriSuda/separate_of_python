import create_cyphercode



def main():
    create_cyphercode.getCountryList()
    country, total_lines = create_cyphercode.getCountryList()
    create_cyphercode.CypherCode_MATCH(country, total_lines)
    


if __name__ == '__main__':
    main()