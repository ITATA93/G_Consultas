# SQLUser.PA_PathwayRole

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHR_ParRef | varchar | PK |  | NO | PA_Pathway Parent Reference |
| PATHR_CareProv_DR | varchar |  | FK | SI | Current Care Provider |
| PATHR_Childsub | double |  |  | NO | Childsub |
| PATHR_Inherited_From_Protocol | bit |  |  | SI | Flag to know whether role comes from protocol, or ... |
| PATHR_Mandatory | varchar |  |  | SI | Mandatory |
| PATHR_Role_DR | bigint |  | FK | SI | Multidisciplinary Team Role |
| PATHR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*