# SQLUser.SS_UserExtSysCodes

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXT_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| EXT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| EXT_Childsub | double |  |  | NO | Childsub |
| EXT_Code | varchar |  |  | SI | Code |
| EXT_DateFrom | date |  |  | SI | Date From |
| EXT_DateTo | date |  |  | SI | DateTo |
| EXT_DefaultSend | varchar |  |  | SI | DefaultSend |
| EXT_Hospital_DR | bigint |  | FK | SI | Des Ref to CT_Hospital |
| EXT_Interface | varchar |  |  | SI | Interface |
| EXT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*