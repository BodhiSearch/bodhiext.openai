from bodhiext.openai import bodhiext_openai_llm_service_builder, bodhilib_list_services


def test_bohilib_list_services():
    services = bodhilib_list_services()
    assert len(services) == 1
    service = services[0]
    assert service.service_name == "openai"
    assert service.service_type == "llm"
    assert service.version == "0.1.0"

def test_bodhiext_openai_llm_service_builder():
    service = bodhiext_openai_llm_service_builder(model="deep thought", api_key="424242")
    service.model = "deep thought"
    service.api_key = "424242"
