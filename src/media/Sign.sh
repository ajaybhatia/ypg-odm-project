#Variables This need to be defined in each signing proces.

#$(target_file_name) example p7201-target_files-1474857792.zip
#$(mmx_key_path)  example /home/gursimran/YUClosed/vendor/yuos/security/yuos_keys
#$(path_of_target_file) example  /home/gursimran/ODM/tinno/dist
#$(new_path_of_signed_target_files) example /home/gursimran/YUClosed
#$(OS_Android_version) example MM-6.0.1
#$(Build_ID) Example MMB30K
#$(mmx_build_version) Example MMXMR1.0
#$(target_product) Example jalebi

#echo "hi"
#echo $target
#echo $2
# Signing ODM GIVEN TARGET FILES
echo $target_file_name
echo $mmx_key_path
echo $path_of_target_file
echo $new_path_of_signed_target_files
echo $OS_Android_version
echo $Build_ID
echo $mmx_build_version
echo $target_product

#./build/tools/releasetools/sign_target_files_apks.py -o -d  /home/gursimran/YUClosed/vendor/yuos/security/yuos_keys/ /home/gursimran/ODM/tinno/dist/*-target_files-*.zip signed-target_files_tinno.zip
./build/tools/releasetools/sign_target_files_apks.py -o -d $mmx_key_path/  $path_of_target_file/$target_file_name $new_path_of_signed_target_files/Signed-MMX-30092016-$OS_Android_version-$Build_ID-$mmx_build_version_$target_product.zip

#Fastboot Images
if [ "$1" == "FACTORY" ] 
then 
echo "Factoryyyyy"
./build/tools/releasetools/img_from_target_files $new_path_of_signed_target_file/Signed-MMX-30092016-$OS_Android_version-$Build_ID-$mmx_build_version_$target_product.zip $new_path_of_signed_target_files/MMX-$OS_Android_version-$Build_ID-$mmx_build_version_$target_product-Signed-fastboot-images-30092016.zip

else
#Signed OTA PACKAGES
echo "ota"
./build/tools/releasetools/ota_from_target_files --block \
   -k $mmx_key_path/releasekey \
 $new_path_of_signed_target_files/Signed-MMX-30092016-$OS_Android_version-$Build_ID-$mmx_build_version_$target_product.zip \
   $new_path_of_signed_target_files/Signed-MMX-30092016-$OS_Android_version-$Build_ID-$mmx_build_version_$target_product-ota.zip
fi
