# TC_hmf_Generator_Lib_Gateway_Process_HL7toSDA3MessageQuery.Context

**Schema:** TC_hmf_Generator_Lib_Gateway_Process_HL7toSDA3MessageQuery
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %LastError | varchar |  |  | SI | This holds last exception |
| %LastFault | varchar |  |  | SI | This holds the last thrown fault |
| %Process | bigint |  |  | SI | This holds the reference to the process object |
| Operation | varchar |  |  | SI | - |
| baseClass | varchar |  |  | SI | - |
| requestTransform | varchar |  |  | SI | - |
| responseTransform | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*