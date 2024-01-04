using Microsoft.AspNetCore.Mvc;

namespace prototype1.Controllers;

[ApiController]
[Route("[controller]")]
public class TestDataController : ControllerBase
{
    private readonly ILogger<TestDataController> _logger;

    public TestDataController(ILogger<TestDataController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetData")]
    public TestData Get()
    {
        return new TestData {
            Val = 230.43,
        };
    }
}
