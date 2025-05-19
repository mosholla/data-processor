import sys

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            values = [float(line.strip()) for line in file if line.strip()]
        return values
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: File contains non-numeric data.")
        sys.exit(1)

def process_data(data):
    if len(data) < 3:
        print("Error: At least 3 data values required.")
        sys.exit(1)
    total = sum(data)
    average = total / len(data)
    return total, average

def write_results(output_file, total, average):
    try:
        with open(output_file, 'w') as file:
            file.write(f"Total: {total}\n")
            file.write(f"Average: {average}\n")
    except IOError:
        print("Error: Could not write to output file.")
        sys.exit(1)

def write_report(log_file, input_file, output_file, count):
    with open(log_file, 'w') as file:
        file.write(f"Input file: {input_file}\n")
        file.write(f"Output file: {output_file}\n")
        file.write(f"Data values processed: {count}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python data_processor.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = 'output_data.txt'
    report_file = 'processing_report.txt'

    data = read_data(input_file)
    total, average = process_data(data)
    write_results(output_file, total, average)
    write_report(report_file, input_file, output_file, len(data))

    print("Processing complete. Results written to output_data.txt and processing_report.txt.")

if __name__ == '__main__':
    main()
