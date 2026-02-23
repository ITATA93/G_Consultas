# SQLUser.SS_UserOtherLogonLoc

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTHLL_CTLOC_DR | bigint | PK | FK | SI | Des Ref CTLOC |
| OTHLL_Childsub | double | PK |  | NO | Childsub |
| OTHLL_DateFrom | date | PK |  | SI | DateFrom |
| OTHLL_DateTo | date | PK |  | SI | DateTo |
| OTHLL_Hospital_DR | bigint | PK | FK | SI | Des Ref to CT_Hospital |
| OTHLL_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| OTHLL_Profile_DR | bigint | PK | FK | SI | Des Ref Access Profile |
| OTHLL_RowId | varchar | PK |  | NO | - |
| OTHLL_UserGroup_DR | bigint | PK | FK | SI | Des Ref UserGroup |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*