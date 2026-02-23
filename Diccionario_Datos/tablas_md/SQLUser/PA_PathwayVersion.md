# SQLUser.PA_PathwayVersion

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHV_ParRef | varchar | PK |  | NO | PA_Pathway Parent Reference |
| PATHV_Childsub | double |  |  | NO | Childsub |
| PATHV_CreateDate | date |  |  | SI | CreateDate |
| PATHV_CreateTime | time |  |  | SI | Create Time |
| PATHV_CreateUser_DR | varchar |  | FK | SI | CreateUser |
| PATHV_Doc_DR | bigint |  | FK | SI | Document Direct Reference |
| PATHV_Path | varchar |  |  | SI | File Path |
| PATHV_ReportDesc | varchar |  |  | SI | ReportDesc |
| PATHV_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*