# SQLUser.CF_SystemFilePath

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATH_ParRef | bigint | PK |  | NO | CF_SystemFileDefinition Parent Reference |
| PATH_Childsub | double |  |  | NO | Childsub |
| PATH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PATH_Path | varchar |  |  | SI | Path |
| PATH_RowId | varchar |  |  | NO | - |
| PATH_UNIXPath | varchar |  |  | SI | UNIXPath |
| Q21Q1 | - |  |  | SI | Hora |
| Q21Q2 | - |  |  | SI | Medicamento |
| Q21Q3 | - |  |  | SI | Dosis |
| Q21Q4 | - |  |  | SI | Vía de Administración |
| Q21Q5 | - |  |  | SI | Responsable |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*