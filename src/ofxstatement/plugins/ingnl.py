import csv

from ofxstatement import statement
from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.parser import StatementParser
from ofxstatement.statement import StatementLine

class IngNlPlugin(Plugin):
    """ING Netherlands Plugin
    """

    def get_parser(self, filename):
        f = open(filename, 'r', encoding=self.settings.get("charset", "UTF-8"))

        return IngNlParser(f)

class IngNlParser(CsvStatementParser):

    date_format = "%Y%m%d"
    mappings = {
        'date': 0,
        'payee': 1,
        'trntype': 5,
        'amount': 6,
        'memo': 8,
    }
    
    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super().parse()

        stmt.account_id = self.acct
        stmt.bank_id = None
        stmt.currency = "EUR"

        statement.recalculate_balance(stmt)

        return stmt

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        
        reader = csv.reader(self.fin, delimiter=',', quotechar='"')

        # Absorb header line
        next(reader, None)

        return reader

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """

        if line[5] in ["Af", "Debit"]:
            line[5] = "DEBIT"
        elif line[5] in ["Bij", "Credit"]:
            line[5] = "CREDIT"

        line[6] = line[6].replace(",", ".")

        self.acct = line[2]

        return super().parse_record(line)

