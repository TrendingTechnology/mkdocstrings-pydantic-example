# Requirements
1. `python=^3.10`
2. `poetry`

# Example
```shell
# Install Dependencies
$ poetry install

# Enter Shell
$ poetry shell

# Serve Docs
$ mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
ERROR    -  Error building page 'index.md': module 'pydantic' has no attribute '_hypothesis_plugin'
Traceback (most recent call last):
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs_autorefs/plugin.py", line 88, in get_item_url
    url = self._url_map[identifier]
KeyError: 'pydantic'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/fakeusername/Desktop/example/.venv/bin/mkdocs", line 8, in <module>
    sys.exit(cli())
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/click/core.py", line 1659, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/__main__.py", line 177, in serve_command
    serve.serve(dev_addr=dev_addr, livereload=livereload, **kwargs)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/commands/serve.py", line 54, in serve
    config = builder()
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/commands/serve.py", line 49, in builder
    build(config, live_server=live_server, dirty=dirty)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/commands/build.py", line 314, in build
    _build_page(file.page, config, doc_files, nav, env, dirty)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/commands/build.py", line 220, in _build_page
    output = config['plugins'].run_event(
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs/plugins.py", line 102, in run_event
    result = method(item, **kwargs)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs_autorefs/plugin.py", line 197, in on_post_page
    fixed_output, unmapped = fix_refs(output, url_mapper)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs_autorefs/references.py", line 186, in fix_refs
    html = AUTO_REF_RE.sub(fix_ref(url_mapper, unmapped), html)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs_autorefs/references.py", line 156, in inner
    url = url_mapper(unescape(identifier))
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocs_autorefs/plugin.py", line 94, in get_item_url
    new_identifiers = fallback(identifier)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocstrings/handlers/base.py", line 408, in get_anchors
    anchors = handler.renderer.get_anchors(handler.collector.collect(identifier, fallback_config))
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/mkdocstrings_handlers/python/collector.py", line 69, in collect
    loader.load_module(module_name)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 131, in load_module
    top_module = self._load_module_path(package.name, package.path, submodules=submodules)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 287, in _load_module_path
    self._load_submodules(module)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 292, in _load_submodules
    self._load_submodule(module, subparts, subpath)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 303, in _load_submodule
    member_parent[subparts[-1]] = self._load_module_path(
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 285, in _load_module_path
    module = self._inspect_module(module_name, module_path, parent)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/loader.py", line 347, in _inspect_module
    module = inspect(
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/agents/inspector.py", line 92, in inspect
    ).get_module(import_paths)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/agents/inspector.py", line 206, in get_module
    value = dynamic_import(import_path, import_paths)
  File "/home/fakeusername/Desktop/example/.venv/lib/python3.10/site-packages/griffe/importer.py", line 67, in dynamic_import
    value = getattr(value, part)
AttributeError: module 'pydantic' has no attribute '_hypothesis_plugin'
```
