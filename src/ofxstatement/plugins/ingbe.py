import csv

from ofxstatement import statement
from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.parser import StatementParser
from ofxstatement.statement import StatementLine

class IngBePlugin(Plugin):
    """ING Belgium Plugin
    """

    def get_parser(self, filename):
        f = open(filename, 'r', encoding=self.settings.get("charset", "ISO-8859-1"))
        parser = IngBeParser(f)
        return parser

class IngBeParser(CsvStatementParser):

    date_format = "%d/%m/%Y"
    mappings = {
        'check_no': 3,
        'date': 5,
        'payee': 2,
        'memo': 8,
        'amount': 6
    }
    
    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        stmt = super(IngBeParser, self).parse()
        statement.recalculate_balance(stmt)
        return stmt

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        
        reader = csv.reader(self.fin, delimiter=';')
        next(reader, None)
        return reader

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """
        
        # Remove non CSV cr*p and zero-value notifications
        if(line[5] and not (line[6]=="0")):          
            transaction_id = line[3]
            date = line[4]
            date_value = line[5]
            if(line[2]):
                account_to = line[2]
            else:
                account_to = line[8]
		    	
            currency = line[7]
            line[6] = line[6].replace(",", ".")
            amount = line[6]

            
            # Pack info in description
            line[8] = line[8]+"-"+line[9]+"-"+line[10]
            description = line[8]

            stmtline = super(IngBeParser, self).parse_record(line)
            stmtline.trntype = 'DEBIT' if stmtline.amount < 0 else 'CREDIT'
        
            return stmtline
