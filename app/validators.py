from django.forms import ValidationError

def validatename(name):
    if len(name)<=2:
        raise ValidationError('name must be more than 2 characters')
    
    
def validate_username(username):
	for i in username:
			if not('a'<=i<='z' or 'A'<=i<='Z'):
				raise ValidationError('Name should be only alpha numberic characters')
			return username
       

def validate_phone_no(phone_no):
		
		if len(str(phone_no))!=10:
			raise ValidationError('Phone Number must consist of 10 digits')
		
		if str(phone_no)[0] not in ['6','7','8','9']:
			raise ValidationError('Invalid Phone Number,Number starts with 6,7,8,9')
		return phone_no

	