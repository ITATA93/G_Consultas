# SQLUser.AR_HICInHospitalClaimRepSubRow

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHCRSR_ParRef | varchar | PK |  | NO | - |
| ChildQ61DR | - |  |  | SI | Child Reference: Actividades de la Vida Diaria y T... |
| IHCRSR_ElementName | varchar |  |  | NO | Name of the element |
| IHCRSR_ElementValue | varchar |  |  | SI | Value of the element |
| IHCRSR_RowID | varchar |  |  | NO | - |
| IHCRSR_SubRowNumber | integer |  |  | NO | Sub-row number |
| Q28Q1 | - |  |  | SI | Actividades |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*