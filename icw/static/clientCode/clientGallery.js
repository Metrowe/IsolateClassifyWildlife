function getImageMarkup(path,label)
{
	return `
		<div class="col-md-4 theme-colour-c">
			<div style="margin:3%">
				<img class="img-responsive border mx-auto d-block" src="${path}" width="100%" ">
			</div>
			<div class="card-body">
				<p class="card-text text-center">
					Animal: ${label}
				</p>
			</div>
		</div>
		`;
}
// style="background-color: rgba(255,255,0,255);
// <img class="img-responsive border mx-auto d-block" src="${path}" width="100%">
// 


function populateGallery(imageList)
{
	let row = document.getElementById("galleryRow");

	// if( Array.isArray(pathList) && pathList.length > 0 )
	if( imageList.length > 0 )
	{
		row.innerHTML = "";

		imageList.forEach(function (image) {
			// console.log(path);
	  		row.innerHTML = row.innerHTML + getImageMarkup(image.path,image.label);
		});
	}
	else
	{
		row.innerHTML = "No results";
	}
}

// async function initialGalleryContents(type,label)
// {
// 	let url = getBaseUrl() + "galleryImages";

// 	let formData = new FormData();
// 	formData.append('type', type);
// 	formData.append('label', label);

// 	let result = await getJsonData(url,{method: "POST", body: formData});

// 	// let results = await getJsonData(url,null);

// 	pathList = results.map(result => result.path);

// 	populateGallery(pathList)

// 	console.log(url);
// 	console.log(results);
// }

async function galleryAttempt()
{
	let url = getBaseUrl() + "galleryrequest";

	let labelElement = document.getElementById('label-input');

	let typeInputElement1 =  document.getElementById('type-input1');
	let typeInputElement2 =  document.getElementById('type-input2');
	let typeInputElement3 =  document.getElementById('type-input3');
	let typeInputElement4 =  document.getElementById('type-input4');

	label = label = labelElement.value.replace(' ', '+');
	type = getCheckedRadioValue(typeInputElement1,typeInputElement2,typeInputElement3,typeInputElement4);
	labelElement.value = '';

	let formData = new FormData();
	formData.append('category', type);
	formData.append('label', label);

	// console.log(type)
	// console.log(label)

	console.log('label: ' + label);

	let results = await getJsonData(url,{method: "POST", body: formData});

	if( Array.isArray(results) )
	{
		let imageList = results.filter(result => result.path != null && result.label != null);
		// let pathList = results.map(result => result.path).filter(path => path != null);
		populateGallery(imageList)
	}
	else
	{
		let errorMessage = 'Search Failed';

		if (results != null && "error" in results) 
		{
	    	errorMessage = results.error;
		}

		displayError(errorMessage);
	}

	console.log(url);
	console.log(results);
}

galleryAttempt()