import os

#stripe
os.environ.setdefault('STRIPE_PUBLISHABLE', "pk_test_xw1BD4o3yGettsXTTOxuOrAM00k7B6gTMb")
os.environ.setdefault('STRIPE_SECRET', "sk_test_R1Vl3skEd4ahbpxKJaXo8a3a00LKvKkGQm")


#databases
os.environ.setdefault("DATABASE_URL", "postgres://lnbqqolahcfyjl:f4f95a3b3d4a5bf4d5074076ab4f79b802862d0d1c10c8d7dead21af092d5ef1@ec2-54-246-121-32.eu-west-1.compute.amazonaws.com:5432/ddgpu1i016mcf7")

#secret_key project
os.environ.setdefault("SECRET_KEY", "$-t*iczx5ohb=%sjbx^9rrb(hq72m-5ng)0#4qhzfie@*+d4^1")


#email smtp
os.environ['EMAIL_USER'] = 'othdur@gmail.com'
os.environ['EMAIL_PASSWORD'] = 'Uniform1'


#aws keys
os.environ.setdefault("AWS_SECRET_KEY_ID", "AKIAXHRH3EJUROI3DPZB")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "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")
