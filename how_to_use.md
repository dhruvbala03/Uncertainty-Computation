# How to use this tool

---------------------------

## UPDATE: You can now use standard arithmetic operators (+-*/) rather than the prefix functions described below. 

---------------------------

### Define values with uncertainty:

val_1 = Value(numerical_val_1, uncertainty_val_1)
val_2 = Value(numerical_val_2, uncertainty_val_2)
val_3 = Value(numerical_val_3, uncertainty_val_3)

### Convert a constant to a value to use in computation:
k = Value.const(0.5)

### Get the negative of a value:
neg_val = val_1.negate()

### Take a value to an exponent:
val_to_pow = val_3.exp(2)

### Multiply two or more values:
product = multu(val_1, val_2, val_3)

### Divide two values:
quotient = divu(val_2, val_3)

### Add two or more values:
sum = addu(val_1, val_3)

### Subtract values:
diff = addu(val_1, val_2.negate())

### Print a value:
print(val_1)

#### Note: functions can be combined, as demonstrated in the subtraction example.

---------------------------

### See demo code at the bottom of main.py for demonstration
