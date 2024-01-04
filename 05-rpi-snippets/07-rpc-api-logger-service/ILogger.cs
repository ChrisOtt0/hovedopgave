using System.Runtime.CompilerServices;

namespace PMTester.Services {
    public enum Severity {
        Trace = 0,
        Debug = 1,
        Information = 2,
        Warning = 3,
        Error = 4,
    }

    public interface ILogger {
        void Log(
            Severity severity, 
            string message, 
            Exception? error,
            [CallerMemberName] string memberName = "", 
            [CallerFilePath] string sourceFilePath = "", 
            [CallerLineNumber] int sourceLineNumber = 0);
    }
}