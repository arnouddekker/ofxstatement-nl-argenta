import csv

from ofxstatement import statement
from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.parser import StatementParser
from ofxstatement.statement import StatementLine

class ArgentaNlPlugin(Plugin):
    """Argenta Netherlands Plugin
    """

    def get_parser(self, filename):
        f = open(filename, 'r', encoding=self.settings.get("charset", "UTF-8"))

        return ArgentaNlParser(f)

class ArgentaNlParser(CsvStatementParser):

    date_format = "%d-%m-%Y"
    mappings = {
        'date': 0,
        'amount': 1,
        'trntype': 2,
        'check_no': 3,
        'payee': 4,
        'memo': 5,
    }
    
    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super().parse()

        stmt.account_id = None
        stmt.bank_id = None
        stmt.currency = "EUR"

        statement.recalculate_balance(stmt)

        return stmt

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        
        reader = csv.reader(self.fin, delimiter=',', quoting=csv.QUOTE_NONE)

        # Absorb header line
        next(reader, None)

        return reader

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """

        if line[2] in ["Debit"]:
            line[2] = "DEBIT"
        elif line[2] in ["Credit"]:
            line[2] = "CREDIT"

        line[1] = line[1].replace(",", ".")

        return super().parse_record(line)

