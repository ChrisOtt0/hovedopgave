import hashlib
import hmac
import rsa

class AAGCrypt:
    def get_checksum(self, symkey: str, path_to_file: str) -> bytes:
        """
        Generates checksum from provided filepath and symmetric key.
        """
        checksum = None

        try:
            sha512 = hmac.new(symkey, digestmod=hashlib.sha512)
            with open(path_to_file, "rb") as f:
                while chunk := f.read(8192):
                    sha512.update(chunk)

            checksum = sha512.hexdigest().encode()
        except Exception as e:
            raise Exception("Could not generate checksum from filepath: {}\n{}".format(path_to_file, e))
        
        return checksum


class AGVerifier(AAGCrypt):
    """
    Class used to verify data integrity of file after transfer.
    Furthermore ensures data received only comes from within the company itself.
    This is done using a symmetric key and an asymmetric key-pair, of which the public key is provided the class.
    """

    def __init__(self, path_pubkey: str, path_symkey: str):
        self.pubkey = None
        self.symkey = None

        # Get public key
        try:
            with open(path_pubkey, "rb") as f:
                self.pubkey = rsa.PublicKey.load_pkcs1(f.read())
        
        except Exception as e:
            raise Exception("Error loading public key from path: {}\n{}".format(path_pubkey, e))
        

        # Get symmetric key
        try:
            with open(path_symkey, "rb") as f:
                self.symkey = f.read()

        except Exception as e:
            raise Exception("Error loading symmetric key from path: {}\n{}".format(path_symkey, e))
        
    
    def verify(self, path_to_file: str, signature: bytes) -> bool:
        """
        Verifies data integrity and ensures sender was from AGRAMKOW.
        """
        checksum = None

        # Generate checksum
        try:
            checksum = self.get_checksum(self.symkey, path_to_file)
        except Exception as e:
            raise e

        # Verify signature
        try:
            _ = rsa.verify(checksum, signature, self.pubkey)
        except:
            return False
        
        return True



class AGSigner(AAGCrypt):
    """
    Class used to sign a file, so it can be verified by the receiver.
    Ensures data integrity, and ensures the receiver of, who the sender is.
    This is done using a symmetric key and an asymmetric key-pair, of which the private key is provided the class.
    """

    def __init__(self, path_privkey: str, path_symkey: str):
        self.privkey = None
        self.symkey = None

        # Get private key
        try:
            with open(path_privkey, "rb") as f:
                self.privkey = rsa.PrivateKey.load_pkcs1(f.read())
        
        except Exception as e:
            raise Exception("Error loading private key from path: {}\n{}".format(path_privkey, e))
        
        # Get symmetric key
        try:
            with open(path_symkey, "rb") as f:
                self.symkey = f.read()

        except Exception as e:
            raise Exception("Error loading symmetric key from path: {}\n{}".format(path_symkey, e))
        

    def sign(self, path_to_file: str) -> bytes:
        """
        Signs the given file at provided filepath and returns the signature.
        """
        checksum = None

        # Generate checksum
        try:
            checksum = self.get_checksum(self.symkey, path_to_file)
        except Exception as e:
            raise e
        
        # Generate signature
        return rsa.sign(checksum, self.privkey, "SHA-512")