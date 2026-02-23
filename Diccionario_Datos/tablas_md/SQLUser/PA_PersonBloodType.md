# SQLUser.PA_PersonBloodType

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLDTP_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| BLDTP_BloodType_DR | bigint |  | FK | NO | Des Ref BloodType |
| BLDTP_Childsub | double |  |  | NO | Childsub |
| BLDTP_DateFrom | date |  |  | SI | [DEPRECATED]Unnecessary Property[/DEPRECATED] Date... |
| BLDTP_DateTo | date |  |  | SI | [DEPRECATED]Unnecessary Property[/DEPRECATED] Date... |
| BLDTP_RowId | varchar |  |  | NO | - |
| BLDTP_Source | varchar |  |  | SI | Source   |
| BLDTP_TestSetItem_DR | varchar |  | FK | SI | Test Set Item from which result is derived |
| BLDTP_UpdateDate | date |  |  | SI | Update Date |
| BLDTP_UpdateTime | time |  |  | SI | Update Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*