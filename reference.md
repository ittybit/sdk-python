# Reference
## Automations
<details><summary><code>client.automations.<a href="src/ittybit/automations/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all automations for the current project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.automations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/ittybit/automations/client.py">create</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new automation for the current project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.automations.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/ittybit/automations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific automation by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.automations.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The automation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/ittybit/automations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing automation by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.automations.update(id='id', name='Transcode Uploaded Videos (Updated)', trigger=[{'event': 'media.ready'
, 'conditions': [{'prop': 'media.kind', 'value': 'image'}]
}], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the automation to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow:** `typing.Optional[typing.Sequence[WorkflowTaskStepParams]]` — The updated sequence of tasks for the automation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/ittybit/automations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an automation by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.automations.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The automation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/ittybit/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of all files associated with the current project. Files can be filtered using query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.files.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">create_from_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a file from a publicly accessible URL. The file will be ingested asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.files.create_from_url(url='https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', filename='BigBuckBunny.mp4', folder='examples/cartoons', metadata={'source': 'google_storage_sample'
}, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — The publicly accessible URL of the file to ingest.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Optional desired filename. If not provided, it may be derived from the URL.
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` — Folder path (optional)
    
</dd>
</dl>

<dl>
<dd>

**media_id:** `typing.Optional[str]` — Optional existing media ID to associate the file with.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Optional label for the file.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional user-defined key-value metadata.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` — Whether to process the ingestion asynchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific file identified by its unique ID, including its metadata, media associations, and technical properties.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.files.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the file to retrieve. Must be a valid file ID (e.g., file_7bKpN2950Dx4EW8T).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently removes a file from the system. This action cannot be undone. Associated media entries may still reference this file ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.files.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the file to delete. Must be a valid file ID (e.g., file_7bKpN2950Dx4EW8T).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">update_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates metadata, filename, or folder properties of an existing file. Only the specified fields will be updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.files.update_metadata(id='id', filename='final_approved_video.mp4', folder='archive/2024', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the file to update. Must be a valid file ID (e.g., file_abc123).
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — An object containing key-value pairs to set or update. Set a key to null to remove it.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — New filename for the file.
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` — New folder path for the file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Media
<details><summary><code>client.media.<a href="src/ittybit/media/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all media for the current project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.media.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of media items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.media.<a href="src/ittybit/media/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new media item from a URL or as an empty placeholder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.media.create(title='Placeholder for User Upload', metadata={'user_id': 'user_789'
}, empty=True, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the media file to ingest. Required unless 'empty' is true.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label for the media
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` — Folder to store the media in
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Filename for the media
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title for the media
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional metadata for the media
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` — Whether to process the media asynchronously
    
</dd>
</dl>

<dl>
<dd>

**empty:** `typing.Optional[bool]` — Create an empty media placeholder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.media.<a href="src/ittybit/media/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific media item by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.media.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The media ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.media.<a href="src/ittybit/media/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific media item by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.media.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The media ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks
<details><summary><code>client.tasks.<a href="src/ittybit/tasks/client.py">list_filtered</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of tasks for the project, optionally filtered by status or kind.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.tasks.list_filtered()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TasksListFilteredRequestStatus]` — Filter by task status.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[TasksListFilteredRequestKind]` — Filter by task kind.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/ittybit/tasks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new processing task (e.g., ingest, video transcode, speech analysis) or a workflow task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.tasks.create(kind="ingest", url='https://example.com/some_video.mov', input={'options': {'filename': 'custom_name.mov'}
}, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kind:** `TasksCreateRequestKind` — The type of task to create.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the source file (required for 'ingest' kind unless file_id is used, can be used for others).
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Task-specific input parameters depending on the kind of task.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — ID of an existing file to use as input (alternative to url).
    
</dd>
</dl>

<dl>
<dd>

**workflow:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` — An array of task definition objects for a workflow.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — An optional HTTPS URL to send a webhook notification to upon task completion or failure.
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Desired filename for the output (if applicable).
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` — Desired output folder (if applicable).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Output format (e.g., for video/image tasks).
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Output width (for video/image tasks).
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Output height (for video/image tasks).
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Output quality setting (e.g., for video/image tasks, 0-100).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/ittybit/tasks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the details of a specific task by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.tasks.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the task to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Signatures
<details><summary><code>client.signatures.<a href="src/ittybit/signatures/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a cryptographically signed URL that provides temporary and restricted access to a file. The URL can expire after a specified time and be limited to specific HTTP methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from ittybit import Ittybit
client = Ittybit(token="YOUR_TOKEN", )
client.signatures.create(filename='video.mp4', folder='private/user_123', expiry=1735689600, method="get", )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filename:** `str` — The name of the file to generate a signature for. Special characters will be sanitised.
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` — Optional folder path where the file resides. Special characters will be sanitised.
    
</dd>
</dl>

<dl>
<dd>

**expiry:** `typing.Optional[int]` — Optional expiry time for the signature in seconds since epoch. Defaults to 60 minutes from now. Must be a positive integer and in the future.
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[SignaturesCreateRequestMethod]` — Optional HTTP method allowed for the signed URL. Defaults to 'get'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

