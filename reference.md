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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.automations.get(
    id="id",
)

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

**id:** `str` 
    
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.automations.update(
    id="id",
    name="Updated Transcoder Example",
    trigger={
        "event": "upload.completed",
        "conditions": [{"prop": "file.type", "value": "image/*"}],
    },
    workflow=[{"kind": "image", "format": "webp"}],
)

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[AutomationsUpdateRequestTriggerParams]` — Defines the trigger event and conditions. To clear/remove a trigger, provide null. To update, provide the new trigger object.
    
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.automations.delete(
    id="id",
)

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

**id:** `str` 
    
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

Retrieves a paginated list of all files associated with the current project.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
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

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new file from a publicly accessible or signed URL.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.files.create(
    url="https://ittyb.it/sample.mp4",
    folder="ittybit/samples",
    filename="video.mp4",
    metadata={"customKey2": "a different custom value"},
)

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

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**media_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ref:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

Retrieve the file object for a file with the given ID.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.files.get(
    id="id",
)

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

**id:** `str` 
    
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

Permanently removes a file from the system. This action cannot be undone.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.files.delete(
    id="id",
)

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

**id:** `str` 
    
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

<details><summary><code>client.files.<a href="src/ittybit/files/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a file's `filename`, `folder`, `ref`, or `metadata`. Only the specified fields will be updated.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.files.update(
    id="id",
    folder="updated/folder",
    filename="new_filename.mp4",
    metadata={"customKey2": "a different custom value"},
)

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ref:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

Retrieves a paginated list of all media for the current project
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
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

**limit:** `typing.Optional[int]` 
    
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

Creates a new media item.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.media.create(
    title="My Video Example",
    alt="An example video used to demonstrate the ittybit API",
    metadata={"customKey2": "a different custom value"},
)

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

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

Retrieves the media object for a media with the given ID.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.media.get(
    id="id",
)

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

**id:** `str` 
    
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

Permanently removes a media object from the system. This action cannot be undone.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.media.delete(
    id="id",
)

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

**id:** `str` 
    
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

<details><summary><code>client.media.<a href="src/ittybit/media/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a media object's `title`, `alt`, or `metadata`. Only the specified fields will be updated.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.media.update(
    id="id",
    title="Updated Video Example",
    alt="An updated example video used to demonstrate the ittybit API",
    metadata={"customKey2": "a different custom value"},
)

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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
<details><summary><code>client.tasks.<a href="src/ittybit/tasks/client.py">list</a>(...)</code></summary>
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.tasks.list()

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

**limit:** `typing.Optional[int]` — Items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TasksListRequestStatus]` — Filter by task status.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[TasksListRequestKind]` — Filter by task kind.
    
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.tasks.create(
    kind="ingest",
    url="https://ittyb.it/sample.mp4",
    filename="bunny-1280x720.mp4",
    folder="examples/cartoons",
    width=1280,
    height=720,
)

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

<details><summary><code>client.tasks.<a href="src/ittybit/tasks/client.py">get_task_config</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves available task kinds and their configuration options.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.tasks.get_task_config()

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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.tasks.get(
    id="id",
)

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

**id:** `str` 
    
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

You can use signatures to create signed URLs which grant access to your project's resources, without revealing your project's API key. URLs can expire after a specified time and be limited to HTTP `GET` method for read-only access, or HTTP `PUT` method for client-side uploads.
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

client = Ittybit(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.signatures.create(
    filename="video.mp4",
    folder="example",
    expiry=1735689600,
    method="put",
)

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

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expiry:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[SignaturesCreateRequestMethod]` 
    
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

