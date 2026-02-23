# SQLUser.AR_HICClaimRepElement

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRE_ParRef | bigint | PK |  | NO | - |
| CRE_ElementName | varchar |  |  | NO | Name of the element |
| CRE_ElementValue | varchar |  |  | SI | Value of the element |
| CRE_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*