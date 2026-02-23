# Region_CLXX_Integration_Nexus_CS_RNI.Dose

**Schema:** Region_CLXX_Integration_Nexus_CS_RNI
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Nexus**. Conexión con sistema externo Nexus.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Campaign | bigint |  |  | SI | - |
| CreateDateTime | timestamp |  |  | NO | - |
| CustomTypeID | varchar |  |  | SI | - |
| DoseCode | varchar |  |  | SI | - |
| DoseDescription | varchar |  |  | SI | - |
| DoseExternalCode | varchar |  |  | SI | - |
| DoseName | varchar |  |  | SI | - |
| Facility | bigint |  |  | SI | - |
| Type | varchar |  |  | SI | Puede ser C o P |
| UpdateDateTime | timestamp |  |  | NO | - |
| VaccineRNI | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*