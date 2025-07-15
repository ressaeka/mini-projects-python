def arithmetic_arranger(problems, show_answers=False):
   #1. Limit a maximum of 5 questions
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = []
    numbers = []
    
  #2. Process each issue
    for problem in problems:
        array = problem.split()
        num1, operator, num2 = array
        
        operators.append(operator)
        numbers.append(num1)
        numbers.append(num2)

   #3. Operator validation
    for op in operators:
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    #4.Number validation
    for num in numbers:
        if not num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    answers = []
    top_row = ''
    bottom_row = ''
    answers_row = ''
    dashes = ''

   #5. Calculation process and display format
    for i in range(0, len(numbers), 2):
        num1 = numbers[i]
        num2 = numbers[i + 1]
        operator = operators[i // 2]

       #6. Calculate results
        if operator == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)
        answers.append(result)

        #7. Specify the format width
        space_width = max(len(num1), len(num2)) + 2
        top_row += num1.rjust(space_width) + '    '
        bottom_row += operator + num2.rjust(space_width - 1) + '    '
        dashes += '-' * space_width + '    '

   #8. Result format if show_answers=True
    if show_answers:
        for i in range(len(answers)):
            space_width = max(len(numbers[2*i]), len(numbers[2*i+1])) + 2
            answers_row += str(answers[i]).rjust(space_width) + '    '

        arranged_problems = '\n'.join([top_row.rstrip(), bottom_row.rstrip(), dashes.rstrip(), answers_row.rstrip()])
    else:
        arranged_problems = '\n'.join([top_row.rstrip(), bottom_row.rstrip(), dashes.rstrip()])

    return arranged_problems


#9. Example of use
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))

