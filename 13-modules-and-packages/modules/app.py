
## importing whole converter module
import converters

## importing specific function from module
from converters import lbs_to_kg

# calling a method of converter object
print(converters.kg_to_lbs(60))

# specific imported functions can be used directly
print(lbs_to_kg(135))