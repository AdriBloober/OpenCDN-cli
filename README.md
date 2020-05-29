# OpenCDN-cli
A cli frontend client for the OpenCDN backend.

## Install
Run the ``install.sh`` with root:  
``sudo ./install.sh``

## Functions

You can run ``opencdn --help`` to get help.  
All commands have this structure: ``opencdn <ACTION> [... OPTIONS]``

### File Target

To target a file you can use the key, filename pair or a link: 

#### Key, filename pair
Use ``-fk <KEY> -ff <FILENAME>``

#### Link
Use ``-fl <LINK>``

### Authentication
If you need authentication, you can use these arguments:  
``-aki`` (``--authentication-key-identifier``): This is the identifier of the key (The variable key name on the server side).
``-akf`` (``--authentication-key-file``): This is the key file, which contains the private key.

### Download
Action name: ``download``  
Requires: File Target and ``-dof`` (``--download-output-file``): The file would be downloaded to this location. You can use in
the filename a ``{FILENAME}``: This would be replaced with the filename of the file.

### Upload
Action name: ``upload``  
Requires: ``-uf`` (``--upload-file``): The path to the uploading file.  
Optional: Authentication and ``-uot`` (``--upload-output-type``): The output, how the cli send the output to you. You can use: ``all, key or link``.

### Delete (File)
Action name: ``delete``  
Requires: File Target, ``-pk`` (``--private-key``): The private key of the file to delete it.

### Check Authentication
Action name: ``check_authentication``  
Requires: Authentication  
Help: Check if your key works.

### Generate Authentication Key
Action name: ``generate_authentication_key``  
Requires: ``-gako``(``--generate-authentication-key-output``): The path to the private key output file.  
Optional: ``-gaks``(``--generate-authentication-key-size``): The size of the key (1024 by default)  
Help: Generates a new authentication key.

### Check Version
Action name: ``check_version``  
Help: Check the version compatibility of the client and server. 

## Upgrading to new version
If you would like to update opencdn-cli you can run the install.sh script again.