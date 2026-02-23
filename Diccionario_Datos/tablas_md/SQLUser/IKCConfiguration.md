# SQLUser.IKCConfiguration

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BlackListId | varchar |  |  | SI | - |
| DomainId | varchar |  |  | SI | - |
| FilterByBlackList | bit |  |  | SI | - |
| FilterByHLC | bit |  |  | SI | - |
| FilterUnmatched | bit |  |  | SI | - |
| UIShowIndexResultsLink | bit |  |  | SI | - |
| UIShowPatientPopulationLink | bit |  |  | SI | - |
| UIShowSettingsLink | bit |  |  | SI | - |
| UIShowSimilarRelatedConcepts | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*