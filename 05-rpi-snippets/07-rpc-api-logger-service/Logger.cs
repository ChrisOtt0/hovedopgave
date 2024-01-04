using System.Diagnostics;
using System.Runtime.CompilerServices;

namespace PMTester.Services {
    public class Logger : ILogger {
        #region Public

        // Logging entrypoint
        public void Log(
            Severity severity,
            string message,
            Exception? error,
            [CallerMemberName] string memberName = "",
            [CallerFilePath] string sourceFilePath = "",
            [CallerLineNumber] int sourceLineNumber = 0) 
        {
            string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
            string sourceFileName = sourceFilePath.Split(Path.DirectorySeparatorChar).Last();

            if (severity < Severity.Error) {
                string content = $"[{timestamp}] {severity}: {message}";
                LogToConsole(content);
            } else {
                if (error is null) {
                    string content = $"[{timestamp}] An unknown error occurred in {sourceFileName}\n\tat {memberName} in {sourceFilePath}:line {sourceLineNumber}";
                    LogToConsole(content);
                } else {
                    string shortform = $"[{timestamp}] An error occured in {sourceFileName}: {error.Message}\n\tat {memberName} in {sourceFilePath}:line {sourceLineNumber}";
                    LogError(shortform, error);
                }
            }
        }

        #endregion
        
        #region Private

        string basePath;

        private void removeDatedLogs() {
            string[] files = Directory.GetFiles(basePath);
            
            foreach (string file in files) {
                string fileDateString = file.Split(Path.DirectorySeparatorChar).Last();
                int year, month;

                if (!Int32.TryParse(fileDateString.Substring(0, 4), out year)) Log(Severity.Error, "Error in pattern of log filenames.", null);
                if (!Int32.TryParse(fileDateString.Substring(5, 2), out month)) Log(Severity.Error, "Error in pattern of log filenames.", null);

                DateTime now = new DateTime(DateTime.Now.Year, DateTime.Now.Month, 1, 0, 0, 0);
                DateTime logDate = new DateTime(year, month, 1, 0, 0, 0);

                if (logDate.AddYears(5) < now) {
                    File.Delete(file);
                }
            }
        }

        [Conditional("DEBUG")]
        private void LogToConsole(string content) {
            Console.WriteLine(content);
        }

        private void LogError(string shortform, Exception error) {
            // Log shortform to Console
            LogToConsole(shortform + $"\nLogs can be found at: {basePath}");

            // Log shortform + content to console
            string content = $"{shortform}\n\n[Message] {error.Message}\n\n[Helplink] {error.HelpLink}\n\n[Stacktrace] {error.StackTrace}\n\n\n";

            LogToFile(content);
        }

        private void LogToFile(string content) {
            string fileName = DateTime.Now.ToString("yyyy-MM_") + "pmtester_log";
            string path = Path.Join(basePath, fileName);

            try {
                using (StreamWriter writer = new StreamWriter(path, true)) {
                    writer.Write(content);
                }
            }
            catch (Exception err) {
                Console.WriteLine($"Could not log message:\n{err.Message}");
            }
        }

        #endregion

        #region Constructor

        public Logger(string basePath) {
            this.basePath = basePath;

            if (!Directory.Exists(basePath)) {
                Directory.CreateDirectory(basePath);
            }

            removeDatedLogs();
        }

        #endregion
    }
}
