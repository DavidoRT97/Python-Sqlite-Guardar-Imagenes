/*
 "Binary Large Object Block", y es una denominación genérica para referirse a todos los datos "grandes". Concretamente en SQL Server tienes IMAGE o su alternativa más moderna, VARBINARY(MAX).
*/

CREATE TABLE IF NOT EXISTS bdImagen (
    "nombreArchivo" TEXT,
    "archivoImagen" BLOB
)