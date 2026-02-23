# websys.UserScript

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ScriptType | varchar |  |  | NO | The type of the script as defined in websys.Standa... |
| TestScript | varchar |  |  | SI | The body of the test script containing the initial... |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUserDR | bigint |  | FK | SI | - |
| UserScript | varchar |  |  | SI | The body of the user script containing the user sc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*